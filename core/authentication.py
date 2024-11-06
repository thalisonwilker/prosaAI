"""Auth"""

import os

from fastapi import Header, HTTPException

API_TOKEN = os.getenv("UAI_API_TOKEN")

# Função de dependência para verificação do token
def verificar_token(authorization: str = Header(...)):
    """Verifica se o token de autorização é válido.
    Args:
        authorization (str): Token de autorização.
    Raises:
        HTTPException: Erro de autenticação.
    """
    if authorization != f"Bearer {API_TOKEN}":
        raise HTTPException(status_code=401, detail="Token de autorização inválido")
    return True
