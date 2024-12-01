"""Testes para a função coletar_noticias."""
import os

import unittest
from unittest.mock import patch
# pylint: disable=import-error
from core.news import coletar_noticias


class TestColetarNoticias(unittest.TestCase):
    """Testa a função coletar_noticias."""

    def setUp(self):
        """Set up test fixtures."""
        os.environ['OPENAI_API_KEY'] = '123'

    def tearDown(self):
        """Tear down test fixtures."""
        del os.environ['OPENAI_API_KEY']

    @patch('core.news.parse_feed')
    # mocking environment variables OPENAI_API_KEY
    @patch.dict(os.environ, {'OPENAI_API_KEY': '123'})
    def test_coletar_noticias_success(self, mock_parse):
        """Testa a função coletar_noticias."""
        # Mocking feedparser.parse to return a predefined structure
        mock_feed = [
            {
                'titulo': 'Notícia 1',
                'descricao': 'Descrição da notícia 1',
                'link': 'http://link1.com'
            },
            {
                'titulo': 'Notícia 2',
                'descricao': 'Descrição da notícia 2',
                'link': 'http://link2.com'
            }
        ]
        mock_parse.return_value = mock_feed

        feeds = ['http://feed1.com', 'http://feed2.com']

        result = coletar_noticias(feeds)
        print(result)

        # check if the  mock parse is called twice
        self.assertEqual(mock_parse.call_count, 2)

        # count the number of news is 4
        # because we have 2 feeds with 2 news each
        self.assertEqual(len(result), 4)


if __name__ == '__main__':
    unittest.main(verbosity=2)
