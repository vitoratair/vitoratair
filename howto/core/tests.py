# -*- coding: utf-8 -*-

from django.test import TestCase

# Create your tests here.
class CoreTest(TestCase):

    """
        Classe responsável pelos métodos de testes referente a app core
    """

    def test_get_home(self):
        """
        GET / must return  status code 200
        """

        response = self.client.get('/')
        self.assertEqual(200, response.status_code)

    def test_template_home(self):
        """
        Template / must return  'index.html'
        """

        response = self.client.get('/')
        self.assertTemplateUsed(response, 'index.html')