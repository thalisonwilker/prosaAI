"""
Contém funções que validam o tema da redação.
"""

import json
import logging

from core.constants import MODEL2, PROVIDER
from core.servico_llm import make_llm_call

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def checar_tema_enem_por_regex(tema):
    """
    Se o tema conter algum termo considerado inapropriado
    a função retorna False.

    Args:
        tema (str): Tema da redação.
    Returns:
        bool: Se o tema é válido ou não.
    """
    termos_inapropriados = [
        "impuros",
        "inadequados",
        "morte",
        "linchamento",
        "limpeza étnica",
    ]
    if any(termo in tema for termo in termos_inapropriados):
        logger.warning("Tema inapropriado: %s", tema)
        return False
    return True


def checar_tema_enem_por_llm(tema):
    """Agente de LLM para checar se o tema da redação é ético.
    Args:
        tema (str): Tema da redação.
    Returns:
        bool: Se o tema é ético ou não.
    """
    contexto = ("Você é um agente de validação ética de temas de "
                "redação do ENEM.")
    tarefa = ("Valide se o tema da redação proposto não "
              "fere os direitos humanos.")
    formato_resposta = {
        "resposta": "sim/não",
        "justificativa": "justificativa da resposta",
    }
    prompt = (
        f"{contexto}\n\n"
        f"{tarefa}\n\n"
        f"### Tema da Redação ###\n"
        f"{tema}\n\n"
        f"Devolva a resposta em formato JSON:\n\n"
        f"{formato_resposta}"
    )
    # Usa um modelo mais poderoso para validar o tema
    # Escala de modelos: gpt-4o-mini < gpt-4o
    logger.info("Validando tema com modelo mais poderoso...")
    response = make_llm_call(PROVIDER, MODEL2, contexto, prompt)
    response = json.loads(response)
    if "sim" in response['resposta']:
        return True
    logger.warning("Tema inapropriado: %s", tema)
    return False
