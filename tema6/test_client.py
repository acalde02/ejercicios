"""Pruebas simples para LLMClient.

Ejecuta:
  python ejercicios/tema6/test_client.py

Nota: si no tienes una API key para un proveedor, el test lo omitirá.
"""

from __future__ import annotations

import os

from llm_client import LLMClient


def _has_env(name: str) -> bool:
    return bool(os.getenv(name))


def main() -> None:
    messages = [
        {
            "role": "system",
            "content": "Eres un asistente conciso. Responde en máximo 2 oraciones.",
        },
        {"role": "user", "content": "¿Qué es Python?"},
    ]

    providers = [
        ("openai", "OPENAI_API_KEY"),
        ("openrouter", "OPENROUTER_API_KEY"),
        ("gemini", "GOOGLE_API_KEY"),
        ("claude", "ANTHROPIC_API_KEY"),
    ]

    for provider, env_name in providers:
        print(f"\n{'=' * 40}")
        print(f"Proveedor: {provider}")
        print(f"{'=' * 40}")

        if not _has_env(env_name):
            print(f"SKIP: falta {env_name}")
            continue

        client = LLMClient(provider)
        text = client.chat(messages, temperature=0.7, max_tokens=200)
        print(f"Respuesta: {text}")

    # Probar streaming con el primer provider disponible.
    print(f"\n{'=' * 40}")
    print("Streaming (primer provider disponible)")
    print(f"{'=' * 40}")

    for provider, env_name in providers:
        if not _has_env(env_name):
            continue
        client = LLMClient(provider)
        for token in client.stream(messages, temperature=0.7, max_tokens=200):
            print(token, end="", flush=True)
        print("\n")
        break
    else:
        print("SKIP: no hay API keys configuradas")


if __name__ == "__main__":
    main()
