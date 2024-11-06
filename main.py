"""Módulo de execução da API."""

from fastapi import FastAPI

from core.constants import NEWS_PATH
from core.news import coletar_noticias, gerar_resumo_e_tema, load_feeds_json

app = FastAPI()


@app.get("/gerar_tema")
def generate_theme():
    """Gera um tema de redação baseado em notícias recentes.
    Args:
        None
    Returns:
        dict: Tema de redação.
    """
    # Coleta as notícias e gera o tema de redação
    news_source = load_feeds_json(NEWS_PATH)
    news_url = [news["URL"] for news in news_source]
    noticias = coletar_noticias(news_url)
    tema = gerar_resumo_e_tema(noticias)
    return {"tema_redacao": tema}
