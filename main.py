from core.news import load_feeds_json
from core.news import coletar_noticias, gerar_resumo_e_tema, load_feeds_json
from core.constants import NEWS_PATH
from fastapi import FastAPI


app = FastAPI()


@app.get("/gerar_tema")
def generate_theme():
    # Coleta as notícias e gera o tema de redação
    news_source = load_feeds_json(NEWS_PATH)
    news_url = [news["URL"] for news in news_source]
    noticias = coletar_noticias(news_url)
    tema = gerar_resumo_e_tema(noticias)
    return {"tema_redacao": tema}
