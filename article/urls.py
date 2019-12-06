# -*- coding: utf-8 -*-
'''
-----------------------------------
    FileName:     urls
    Description:  
    Author:       瓦都尅
    Date:         2019/11/19
-----------------------------------
'''
from django.conf.urls import url

from . import views

app_name = 'article'
urlpatterns = [
    url(r'(?P<article_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'(?P<article_id>[0-9]+)/edit$', views.edit, name='edit'),
    url(r'^add/', views.add, name='add'),
]