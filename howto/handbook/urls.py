# coding: utf-8
from django.conf.urls import patterns, include, url


urlpatterns = patterns('howto.handbook.views',
    url(r'^linux/', 'linux', name='linux'),
    url(r'^pythonOO/', 'pythonOO', name='python'),    
    url(r'^pythonData/', 'pythonData', name='python'),
    url(r'^pythonFirst/', 'pythonFirst', name='python'),
    url(r'^pythonStart/', 'pythonStart', name='python'),
    url(r'^python/', 'python', name='python'),     
)





