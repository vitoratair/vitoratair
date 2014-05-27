# coding: utf-8
from django.shortcuts import render


def python(request):
    """ 
    	Esse método tem por objetivo exibir o template da página sobre python
    """

    return render(request, 'python/index.html')	

def pythonStart(request):
    """ 
    	Esse método tem por objetivo exibir o template da página "O começo de tudo" sobre python
    """

    return render(request, 'python/start.html')    