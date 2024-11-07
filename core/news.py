"""Módulo para coleta e processamento de notícias."""

import json
import logging
import os
import random

import feedparser
from openai import OpenAI
from core.exceptions import ParserError

client = OpenAI(api_key = os.getenv("OPENAI_API_KEY"))
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def coletar_noticias(feeds):
    """Coleta e consolida notícias dos feeds RSS.
    Args:
        feeds (list): Lista de URLs de feeds RSS.
    Returns:
        list: Lista de notícias.
    """
    noticias = []
    for feed_url in feeds:
        feed = feedparser.parse(feed_url)
        for entry in feed['entries']:
            try:
                noticias.append({
                    "titulo": entry.title,
                    "descricao": entry.description,
                    "link": entry.link
                })
            except ParserError as e:
                logger.error("Erro ao coletar notícia: %s", e)
    return noticias



def gerar_resumo_e_tema(noticias):
    """Gera um resumo e um tema de redação baseado nas notícias fornecidas.
    Args:
        noticias (list): Lista de notícias.
    Returns:
        str: Resumo e tema de redação
    """

    random.shuffle(noticias)
    # embaralha as notícias e seleciona as 3 primeiras
    noticias = noticias[:3]
    # Consolida descrições das notícias em um único texto
    texto_noticias = " ".join([noticia["descricao"] for noticia in noticias])
    response_schema = {
        "resumo": "resumo dos principais temas abordados",
        "tema": "Tema da redação sugerido em português",
        "instrucoes": "instruções em português"
    }
    prompt = (
        f"Aqui está um conjunto de notícias recentes:\n\n"
        f"{texto_noticias}\n\n"
        f"1. Forneça um resumo dos principais temas abordados.\n"
        f"2. Sugira um tema de redação com título e instruções em português.\n\n"
        f"3. Devolva a resposta em formato JSON. O  JSON deve conter {response_schema}"
    )

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        response_format={ "type": "json_object" },
        messages=[
        {"role": "system", "content": "Você é gerador de temas de redação no Formato ENEM"},
        {"role": "user", "content": prompt},
        ],
    )

    return response.choices[0].message.content


def load_feeds_json(path_to_json):
    """Carrega feeds RSS de um arquivo JSON.
    Args:
        path_to_json (str): Caminho para o arquivo JSON.
    Returns:
        list: Lista de feeds RSS.

    """
    with open(path_to_json, "r", encoding="utf-8") as file:
        feeds = json.load(file)
    return feeds
