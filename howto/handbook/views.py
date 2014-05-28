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

def pythonFirst(request):
    """ 
        Esse método tem por objetivo exibir o template da página "Primeiro programa" sobre python
    """

    return render(request, 'python/first.html') 

def pythonData(request):
    """ 
        Esse método tem por objetivo exibir o template da página "Tipos de dados" sobre python
    """

    return render(request, 'python/data.html')         