from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
	url(r'', include('howto.core.urls', namespace='core')),    
    url(r'^linux/', 'howto.handbook.views.linux', name='linux'),
    url(r'^pythonOO/', 'howto.handbook.views.pythonOO', name='python'),    
    url(r'^pythonData/', 'howto.handbook.views.pythonData', name='python'),
    url(r'^pythonFirst/', 'howto.handbook.views.pythonFirst', name='python'),
    url(r'^pythonStart/', 'howto.handbook.views.pythonStart', name='python'),
    url(r'^python/', 'howto.handbook.views.python', name='python'),    
    url(r'^admin/', include(admin.site.urls)),
)
