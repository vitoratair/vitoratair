from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',	
	url(r'^handbook/', include('howto.handbook.urls', namespace='handbook')),       
    url(r'^admin/', include(admin.site.urls)),
    url(r'', include('howto.core.urls', namespace='core')),
)
