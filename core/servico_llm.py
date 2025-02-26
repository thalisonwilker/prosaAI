"""
Contem os métodos de Interação os modelos de linguagem.
"""

import logging
import os

from openai import OpenAI

from core.chat_api import ChatAPI

logging.basicConfig(level=logging.INFO)

logger = logging.getLogger(__name__)


def make_llm_call(provider, model, contexto, prompt, api_key=""):
    llm = ChatAPI(provider, model, api_key)
    return llm.gera_conteudo(contexto, prompt)

def make_openai_call(contexto, prompt, model_choice="gpt-4o-mini"):
    OPENAI_CLIENT = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
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
