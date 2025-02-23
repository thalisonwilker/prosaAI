"""Módulo de execução da API."""

import json

from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from openai import OpenAIError

from core.constants import NEWS_PATH
from core.news import coletar_noticias, gerar_resumo_e_tema, load_feeds_json

app = FastAPI()


@app.get("/gerar_tema")
def gerar_tema():
    """
    Gera um tema de redação baseado em notícias recentes.
    Args:
        None
    Returns:
        dict: Tema de redação.
    """
    # Coleta as notícias e gera o tema de redação
    fonte_noticias = load_feeds_json(NEWS_PATH)
    news_url = [news["URL"] for news in fonte_noticias]
    noticias = coletar_noticias(news_url)

    try:
        resumo_e_tema = gerar_resumo_e_tema(noticias)
        resumo_e_tema = json.loads(resumo_e_tema)
    except OpenAIError as error_summary:
        return JSONResponse(content={"error": str(error_summary)})

    # extrai o JSON
    tema_json = jsonable_encoder(resumo_e_tema)
    return JSONResponse(content=tema_json)
