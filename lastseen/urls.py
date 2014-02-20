from django.conf.urls import patterns, url

from lastseen import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index')
)