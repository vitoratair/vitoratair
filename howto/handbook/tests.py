# -*- coding: utf-8 -*-

from django.test import TestCase

# Create your tests here.
class CoreTest(TestCase):

    """
        Classe responsável pelos métodos de testes referente a app handbook
    """

    def test_get_python(self):
        """
        GET / must return  status code 200
        """

        response = self.client.get('/python/')
        self.assertEqual(200, response.status_code)

    def test_template_python(self):
        """
        Template / must return  'python/index.html'
        """

        response = self.client.get('/python/')
        self.assertTemplateUsed(response, 'python/index.html')

    def test_get_pythonStart(self):
        """
        GET / must return  status code 200
        """

        response = self.client.get('/pythonStart/')
        self.assertEqual(200, response.status_code)

    def test_template_pythonStart(self):
        """
        Template / must return  'python/index.html'
        """

        response = self.client.get('/pythonStart/')
        self.assertTemplateUsed(response, 'python/start.html') 

    def test_get_pythonData(self):
        """
        GET / must return  status code 200
        """

        response = self.client.get('/pythonData/')
        self.assertEqual(200, response.status_code)

    def test_template_pythonData(self):
        """
        Template / must return  'python/data.html'
        """

        response = self.client.get('/pythonData/')
        self.assertTemplateUsed(response, 'python/data.html')                