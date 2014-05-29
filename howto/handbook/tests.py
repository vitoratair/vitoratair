# -*- coding: utf-8 -*-

from django.test import TestCase
from django.core.urlresolvers import reverse as r

# Create your tests here.
class CoreTest(TestCase):

    """
        Classe responsável pelos métodos de testes referente a app handbook
    """

    def test_get_python(self):
        """
        GET / must return  status code 200
        """

        response = self.client.get(r('handbook:python'))
        self.assertEqual(200, response.status_code)

    def test_template_python(self):
        """
        Template / must return the correct template used to python page
        """

        response = self.client.get(r('handbook:python'))
        self.assertTemplateUsed(response, 'python/index.html')

    def test_template_python_page1(self):
        """
        Template / must return the correct template used to python page
        """

        response = self.client.get(r('handbook:python', args=['1']))
        self.assertTemplateUsed(response, 'python/start.html')

    def test_template_python_page2(self):
        """
        Template / must return the correct template used to python page
        """

        response = self.client.get(r('handbook:python', args=['2']))
        self.assertTemplateUsed(response, 'python/first.html')

    def test_template_python_page3(self):
        """
        Template / must return the correct template used to python page
        """

        response = self.client.get(r('handbook:python', args=['3']))
        self.assertTemplateUsed(response, 'python/data.html')

    def test_template_python_page4(self):
        """
        Template / must return the correct template used to python page
        """

        response = self.client.get(r('handbook:python', args=['4']))
        self.assertTemplateUsed(response, 'python/oo_1.html')                        

    def test_get_linux(self):
        """
        GET / must return  status code 200
        """

        response = self.client.get(r('handbook:linux'))
        self.assertEqual(200, response.status_code)

    def test_template_linux(self):
        """
        Template / must return the correct template used to linux page
        """

        response = self.client.get(r('handbook:linux'))
        self.assertTemplateUsed(response, 'linux/index.html') 

    def test_template_linux_page1(self):
        """
        Template / must return the correct template used to linux page
        """

        response = self.client.get(r('handbook:linux', args=['1']))
        self.assertTemplateUsed(response, 'linux/linux.html') 

    def test_template_linux_page2(self):
        """
        Template / must return the correct template used to linux page
        """

        response = self.client.get(r('handbook:linux', args=['2']))
        self.assertTemplateUsed(response, 'linux/makefile.html') 

    def test_template_linux_page3(self):
        """
        Template / must return the correct template used to linux page
        """

        response = self.client.get(r('handbook:linux', args=['3']))
        self.assertTemplateUsed(response, 'linux/git.html') 

    def test_template_linux_page4(self):
        """
        Template / must return the correct template used to linux page
        """

        response = self.client.get(r('handbook:linux', args=['4']))
        self.assertTemplateUsed(response, 'linux/workflow.html') 

    def test_template_linux_page5(self):
        """
        Template / must return the correct template used to linux page
        """

        response = self.client.get(r('handbook:linux', args=['5']))
        self.assertTemplateUsed(response, 'linux/branches.html') 



