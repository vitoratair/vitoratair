# coding: utf-8
from django.shortcuts import render


def python(request):
    """ 
    	Esse método tem por objetivo exibir o template da página sobre python
    """

    return render(request, 'python/index.html')	