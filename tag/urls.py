# -*- coding: utf-8 -*-
'''
-----------------------------------
    FileName:     urls
    Description:  
    Author:       瓦都尅
    Date:         2019/11/20
-----------------------------------
'''
from django.conf.urls import url

from . import views

app_name = 'tag'
urlpatterns = [
    url(r'^$', views.tag_index, name='tag_index'),
]