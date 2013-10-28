from django.conf.urls import patterns, include, url

from url.shortener import urls

urlpatterns = patterns('',
    url(r'^shortener/', include(urls)),
)
