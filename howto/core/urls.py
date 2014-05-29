# coding: utf-8
from django.conf.urls import patterns, include, url


urlpatterns = patterns('howto.core.views',
    url(r'^$', 'home', name='home'),
	url(r'^bike/', 'bike', name='bike'),
)
