# coding: utf-8
from django.conf.urls import patterns, include, url


urlpatterns = patterns('howto.handbook.views',
    url(r'^linux/$', 'linux', name='linux'),
    url(r'^linux/(\d+)/$', 'linux', name='linux'),
    url(r'^python/$', 'python', name='python'),
    url(r'^python/(\d+)/$', 'python', name='python'),
)





