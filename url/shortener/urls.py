from django.conf.urls import patterns, url

from url.shortener import views

urlpatterns = patterns('',
    url(r'^list/$', views.shortened_list, name='shortened_list'),
    url(r'^delete/(?P<url_id>\d+)$', views.url_delete, name='url_delete'),
    url(r'^redirect/(?P<url_id>\d+)$', views.url_redirect, name='url_redirect'),
)
