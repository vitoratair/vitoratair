from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^pythonData/', 'howto.handbook.views.pythonData', name='python'),
    url(r'^pythonFirst/', 'howto.handbook.views.pythonFirst', name='python'),
    url(r'^pythonStart/', 'howto.handbook.views.pythonStart', name='python'),
    url(r'^python/', 'howto.handbook.views.python', name='python'),
    url(r'^bike/', 'howto.core.views.bike', name='bike'),
    url(r'^$', 'howto.core.views.home', name='home'),
    url(r'^admin/', include(admin.site.urls)),
)
