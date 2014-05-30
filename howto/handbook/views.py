# coding: utf-8
from django.shortcuts import render

def python(request, url = None):
    """ 
    	Esse método tem por objetivo exibir o template da página sobre python
    """

    if url is None:    
        return render(request, 'python/index.html')	

    elif url == '1':
        return render(request, 'python/start.html')         

    elif url == '2':
        return render(request, 'python/first.html') 
 
    elif url == '3':
        return render(request, 'python/data.html')
    
    elif url == '4':
        return render(request, 'python/tdd.html')        


def linux(request, url = None):
    """ 
        Esse método tem por objetivo exibir o template da página sobre linux
    """

    if url is None:
        return render(request, 'linux/index.html')

    elif url == '1':
        return render(request, 'linux/linux.html')
    
    elif url == '2':
        return render(request, 'linux/makefile.html') 
    
    elif url == '3':
        return render(request, 'linux/git.html')               

    elif url == '4':
        return render(request, 'linux/workflow.html') 

    elif url == '5':
        return render(request, 'linux/branches.html') 

    elif url == '6':
        return render(request, 'linux/git-basic.html')   

    elif url == '7':
        return render(request, 'linux/git-intermediate.html')                               
    
    elif url == '8':
        return render(request, 'linux/git-advanced.html')  
