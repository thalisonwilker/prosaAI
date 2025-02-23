"""Funções utilitárias para processamento de texto."""
import unicodedata


def remover_acentos(txt):
    """
    Remove acentos de um texto.

    Args:
        txt (str): Texto.
    Returns:
        str: Texto sem acentos.
    """

    return ''.join(
        (c for c in unicodedata.normalize('NFD', txt)
         if unicodedata.category(c) != 'Mn')
    )
