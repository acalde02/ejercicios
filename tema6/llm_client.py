"""Cliente unificado para múltiples proveedores de LLMs.

Soporta providers:
- openai: API de OpenAI usando el SDK `openai`
- openrouter: OpenRouter como proxy (SDK `openai` con `base_url`)
- gemini: Google Gemini usando `google-generativeai`
- claude: Anthropic Claude usando `anthropic`

El formato de mensajes de entrada es el unificado estilo OpenAI:
    [{"role": "system"|"user"|"assistant", "content": "..."}, ...]
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Dict, Generator, Iterable, List, Optional, Tuple
import os


def _maybe_load_dotenv() -> None:
    try:
        from dotenv import load_dotenv  # type: ignore

        load_dotenv()
    except Exception:
        # Si python-dotenv no está instalado o falla, no bloqueamos.
        pass


_maybe_load_dotenv()


Message = Dict[str, str]


@dataclass
class _AdaptedClaude:
    system: str
    messages: List[Dict[str, str]]


@dataclass
class _AdaptedGemini:
    history: List[Dict[str, Any]]
    prompt: str


class LLMClient:
    """Cliente unificado para múltiples proveedores de LLMs."""

    DEFAULT_MODELS: Dict[str, str] = {
        "openai": "gpt-4o-mini",
        "gemini": "gemini-1.5-flash",
        "claude": "claude-3-5-haiku-latest",
        "openrouter": "google/gemini-2.0-flash-exp:free",
    }

    def __init__(self, provider: str, model: Optional[str] = None):
        provider = provider.strip().lower()
        if provider not in self.DEFAULT_MODELS:
            raise ValueError(
                f"Proveedor no soportado: {provider}. Usa: {list(self.DEFAULT_MODELS.keys())}"
            )

        self.provider = provider
        self.model = model or self.DEFAULT_MODELS[provider]

        self._client: Any = None
        self._init_provider_client()

    def _require_env(self, name: str) -> str:
        value = os.getenv(name)
        if not value:
            raise ValueError(
                f"Falta la variable de entorno {name}. Añádela a tu .env o entorno."
            )
        return value

    def _init_provider_client(self) -> None:
        if self.provider in ("openai", "openrouter"):
            from openai import OpenAI  # type: ignore

            if self.provider == "openai":
                self._require_env("OPENAI_API_KEY")
                self._client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
            else:
                self._require_env("OPENROUTER_API_KEY")
                self._client = OpenAI(
                    base_url="https://openrouter.ai/api/v1",
                    api_key=os.getenv("OPENROUTER_API_KEY"),
                )
            return

        if self.provider == "gemini":
            try:
                import google.generativeai as genai  # type: ignore
            except ImportError as e:
                raise ImportError(
                    "Para usar Gemini instala: pip install google-generativeai"
                ) from e

            api_key = self._require_env("GOOGLE_API_KEY")
            genai.configure(api_key=api_key)
            self._client = genai
            return

        if self.provider == "claude":
            try:
                import anthropic  # type: ignore
            except ImportError as e:
                raise ImportError("Para usar Claude instala: pip install anthropic") from e

            api_key = self._require_env("ANTHROPIC_API_KEY")
            self._client = anthropic.Anthropic(api_key=api_key)
            return

        raise AssertionError("Provider no manejado")

    def _split_system(self, messages: List[Message]) -> Tuple[str, List[Message]]:
        system_parts: List[str] = []
        non_system: List[Message] = []
        for m in messages:
            role = m.get("role")
            content = m.get("content", "")
            if role == "system":
                system_parts.append(content)
            else:
                non_system.append({"role": role, "content": content})
        return ("\n\n".join(system_parts).strip(), non_system)

    def _adapt_messages_for_claude(self, messages: List[Message]) -> _AdaptedClaude:
        system, non_system = self._split_system(messages)

        claude_messages: List[Dict[str, str]] = []
        for m in non_system:
            role = m["role"]
            if role not in ("user", "assistant"):
                raise ValueError(f"Rol no soportado para Claude: {role}")
            claude_messages.append({"role": role, "content": m["content"]})

        return _AdaptedClaude(system=system, messages=claude_messages)

    def _adapt_messages_for_gemini(self, messages: List[Message]) -> _AdaptedGemini:
        system, non_system = self._split_system(messages)

        # Gemini no soporta system nativo: lo inyectamos al primer mensaje de usuario.
        if system:
            injected = f"[INSTRUCCIONES DEL SISTEMA]\n{system}\n\n"
            for idx, m in enumerate(non_system):
                if m["role"] == "user":
                    non_system[idx] = {"role": "user", "content": injected + m["content"]}
                    break
            else:
                non_system.insert(0, {"role": "user", "content": injected.strip()})

        if not non_system:
            raise ValueError("Se requiere al menos un mensaje no-system")

        # Convertir al formato de historia de Gemini.
        converted: List[Tuple[str, str]] = []
        for m in non_system:
            role = m["role"]
            if role == "user":
                converted.append(("user", m["content"]))
            elif role == "assistant":
                converted.append(("model", m["content"]))
            else:
                raise ValueError(f"Rol no soportado para Gemini: {role}")

        last_role, last_content = converted[-1]
        history_pairs = converted[:-1]

        history = [{"role": r, "parts": [c]} for (r, c) in history_pairs]
        prompt = last_content if last_role == "user" else "Continúa."  # fallback

        return _AdaptedGemini(history=history, prompt=prompt)

    def chat(self, messages: List[Message], **kwargs: Any) -> str:
        """Envía mensajes y retorna la respuesta como string."""

        temperature = kwargs.pop("temperature", None)
        max_tokens = kwargs.pop("max_tokens", None)

        if kwargs:
            # Mantener interfaz simple y consistente.
            raise TypeError(f"Parámetros no soportados: {list(kwargs.keys())}")

        if self.provider in ("openai", "openrouter"):
            response = self._client.chat.completions.create(
                model=self.model,
                messages=messages,
                temperature=temperature,
                max_tokens=max_tokens,
            )
            return response.choices[0].message.content

        if self.provider == "gemini":
            adapted = self._adapt_messages_for_gemini(messages)

            generation_config: Dict[str, Any] = {}
            if temperature is not None:
                generation_config["temperature"] = float(temperature)
            if max_tokens is not None:
                generation_config["max_output_tokens"] = int(max_tokens)

            model = self._client.GenerativeModel(
                self.model,
                generation_config=generation_config or None,
            )
            chat = model.start_chat(history=adapted.history)
            response = chat.send_message(adapted.prompt)
            return response.text

        if self.provider == "claude":
            adapted = self._adapt_messages_for_claude(messages)
            response = self._client.messages.create(
                model=self.model,
                system=adapted.system or None,
                messages=adapted.messages,
                temperature=temperature,
                max_tokens=int(max_tokens) if max_tokens is not None else 1024,
            )
            return response.content[0].text

        raise AssertionError("Provider no manejado")

    def stream(self, messages: List[Message], **kwargs: Any) -> Generator[str, None, None]:
        """Envía mensajes y produce tokens/fragmentos de la respuesta."""

        temperature = kwargs.pop("temperature", None)
        max_tokens = kwargs.pop("max_tokens", None)

        if kwargs:
            raise TypeError(f"Parámetros no soportados: {list(kwargs.keys())}")

        if self.provider in ("openai", "openrouter"):
            stream = self._client.chat.completions.create(
                model=self.model,
                messages=messages,
                temperature=temperature,
                max_tokens=max_tokens,
                stream=True,
            )
            for chunk in stream:
                delta = chunk.choices[0].delta
                content = getattr(delta, "content", None)
                if content:
                    yield content
            return

        if self.provider == "gemini":
            adapted = self._adapt_messages_for_gemini(messages)

            generation_config: Dict[str, Any] = {}
            if temperature is not None:
                generation_config["temperature"] = float(temperature)
            if max_tokens is not None:
                generation_config["max_output_tokens"] = int(max_tokens)

            model = self._client.GenerativeModel(
                self.model,
                generation_config=generation_config or None,
            )
            chat = model.start_chat(history=adapted.history)
            for chunk in chat.send_message(adapted.prompt, stream=True):
                text = getattr(chunk, "text", None)
                if text:
                    yield text
            return

        if self.provider == "claude":
            adapted = self._adapt_messages_for_claude(messages)

            # Streaming en Anthropic se expone como context manager.
            with self._client.messages.stream(
                model=self.model,
                system=adapted.system or None,
                messages=adapted.messages,
                temperature=temperature,
                max_tokens=int(max_tokens) if max_tokens is not None else 1024,
            ) as stream:
                for text in stream.text_stream:
                    if text:
                        yield text
            return

        raise AssertionError("Provider no manejado")
