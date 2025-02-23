"""Teste para as guardrails."""

import unittest
from core.guardrails import (
    checar_tema_enem_semantica,
    checar_tema_enem_analise_sintatica,
    checar_tema_enem_por_llm,
)


class TestGuardrails(unittest.TestCase):
    """Testa as guardrails."""

    def test_checar_tema_enem_semantica_valid(self):
        """Testa se o tema é valido."""
        tema = "A importância da educação"
        self.assertTrue(checar_tema_enem_semantica(tema))

    def test_checar_tema_enem_semantica_invalid(self):
        """Testa se o tema é invalido - semantica."""
        tema = "A importância da limpeza étnica"
        self.assertFalse(checar_tema_enem_semantica(tema))

    def test_checar_tema_enem_analise_sintatica_valid(self):
        """Testa se o tema é valido - semantica."""
        tema = "A importância da educação"
        self.assertTrue(checar_tema_enem_analise_sintatica(tema))

    def test_checar_tema_enem_analise_sintatica_invalid(self):
        """Testa se o tema é invalido - sintatica."""
        tema = "A importância do linchamento"
        self.assertFalse(checar_tema_enem_analise_sintatica(tema))

    def test_checar_tema_enem_por_llm_valid(self):
        """Testa se o tema é invalido - LLM."""
        tema = "A importância da educação"
        self.assertTrue(checar_tema_enem_por_llm(tema))

    def test_checar_tema_enem_por_llm_invalid(self):
        """Testa se o tema é invalido - LLM."""
        tema = "A importância da limpeza étnica"
        self.assertFalse(checar_tema_enem_por_llm(tema))


if __name__ == '__main__':
    unittest.main()
