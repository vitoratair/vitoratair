# -*- coding: utf-8 -*-

from django.test import TestCase
from django.core.urlresolvers import reverse as r

# Create your tests here.
class CoreTest(TestCase):

    """
        Classe responsável pelos métodos de testes referente a app core
    """

    def test_get_home(self):
        """
        GET / must return  status code 200
        """

        response = self.client.get(r('core:home'))
        self.assertEqual(200, response.status_code)

    def test_template_home(self):
        """
        Template / must return  'index.html'
        """

        response = self.client.get(r('core:home'))
        self.assertTemplateUsed(response, 'index.html')

    def test_get_bike(self):
        """
        GET / must return  status code 200
        """

        response = self.client.get(r('core:bike'))
        self.assertEqual(200, response.status_code)

    def test_template_bike(self):
        """
        Template / must return  'bike.html'
        """

        response = self.client.get(r('core:bike'))
        self.assertTemplateUsed(response, 'bike.html')        