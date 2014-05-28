# coding: utf-8
from django.shortcuts import render

def home(request):
    """ 
    	Esse método tem por objetivo exibir o template da página inicial
    """

    return render(request, 'index.html')

def bike(request):
    """ 
    	Esse método tem por objetivo exibir o template da página referente a bike
    """

    return render(request, 'bike.html')    
