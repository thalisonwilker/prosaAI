"""
Contem os métodos de Interação os modelos de linguagem.
"""

import logging
import os

from openai import OpenAI

OPENAI_CLIENT = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
logging.basicConfig(level=logging.INFO)

logger = logging.getLogger(__name__)


def make_llm_call(provider, model, contexto, prompt):
    """
    Criar uma chamada para o modelo de linguagem.
    Cria uma camada de abstração para a chamada do modelo de linguagem.
    Args:
        provider (str): Provedor do modelo
        model (str): Modelo
        contexto (str): Contexto
        prompt (str): Prompt
    Returns:
        response: Resposta do modelo
    """
    if provider == "openai":
        response = make_openai_call(contexto, prompt, model)
        return response
    raise ValueError("Provedor não suportado.")


def make_openai_call(contexto, prompt, model_choice="gpt-4o-mini"):
    """
    Faz a chamada para o modelo OpenAI.
    Arsgs:
        contexto (str): Contexto
        prompt (str): Prompt
        client (OpenAI): Cliente OpenAI
        model_choice (str): Modelo OpenAI
    Returns:
        response: Resposta do modelo
    """
    response = OPENAI_CLIENT.chat.completions.create(
        model=model_choice,
        response_format={"type": "json_object"},
        messages=[
            {"role": "system", "content": contexto},
            {"role": "user", "content": prompt},
        ],
    )
    return response.choices[0].message.content
