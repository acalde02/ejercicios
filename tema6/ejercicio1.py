import os
from openai import OpenAI
from dotenv import load_dotenv

# Cargar variables de entorno
load_dotenv()

# TODO: Crear el cliente
# Opción A - OpenAI directo:
#   client = OpenAI()
# Opción B - OpenRouter (gratuito): 
client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=os.getenv("OPENROUTER_API_KEY"),
)


# TODO: Realizar la llamada a la API
# Opción A - OpenAI: model="gpt-4o-mini"
# Opción B - OpenRouter: model="google/gemini-2.0-flash-exp:free"
# Envía un mensaje de usuario: "¿Qué es el machine learning? Responde en 3 oraciones."
response = client.chat.completions.create(
    model="arcee-ai/trinity-large-preview:free",
    messages=[
        {"role": "user", "content": "¿Qué es el machine learning? Responde en 3 oraciones."}
    ],
    temperature=1.5
)

# TODO: Extraer e imprimir los siguientes datos:
# 1. El texto de la respuesta
print("Respuesta:", response.choices[0].message.content)

# 2. El modelo utilizado
print("Modelo:", response.model)

# 3. Tokens del prompt
print("Prompt tokens:", response.usage.prompt_tokens)

# 4. Tokens de la respuesta
print("Completion tokens:", response.usage.completion_tokens)

# 5. Total de tokens
print("Total tokens:", response.usage.total_tokens)