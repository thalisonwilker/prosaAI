from openai import OpenAI
import feedparser
import json
import os
import logging
import random


client = OpenAI(api_key = os.getenv("OPENAI_API_KEY"))
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def coletar_noticias(feeds):
    """Coleta e consolida notícias dos feeds RSS."""
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
            except Exception as e:
                logger.error(f"Erro ao coletar notícia: {e}")
                pass
    return noticias



def gerar_resumo_e_tema(noticias):
    """Gera um resumo e um tema de redação baseado nas notícias fornecidas."""

    random.shuffle(noticias)
    # embaralha as notícias e seleciona as 3 primeiras
    noticias = noticias[:3]
    # Consolida descrições das notícias em um único texto
    texto_noticias = " ".join([noticia["descricao"] for noticia in noticias])

    prompt = (
        f"Aqui está um conjunto de notícias recentes:\n\n"
        f"{texto_noticias}\n\n"
        f"1. Forneça um resumo dos principais temas abordados.\n"
        f"2. Sugira um tema de redação com título e instruções em português.\n\n"
    )

    response = client.chat.completions.create(
        model="gpt-3.5-turbo-0125",
        messages=[
        {"role": "system", "content": "Você é gerador de temas de redação no Formato ENEM"},
        {"role": "user", "content": prompt},
        ],
    )

    return response.choices[0].message.content


def load_feeds_json(path_to_json):
    """Carrega feeds RSS de um arquivo JSON."""
    with open(path_to_json, "r") as file:
        feeds = json.load(file)
    return feeds