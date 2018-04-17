# -*- coding: utf-8 -*-

from django.conf.urls import include, url
from blog import views

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^update-after/(?P<id>\d+)/$', views.updates_after, name='updates_after'),
]
