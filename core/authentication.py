from fastapi import Header, HTTPException
import os


API_TOKEN = os.getenv("UAI_API_TOKEN")

# Função de dependência para verificação do token
def verificar_token(authorization: str = Header(...)):
    if authorization != f"Bearer {API_TOKEN}":
        raise HTTPException(status_code=401, detail="Token de autorização inválido")