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

app_name = 'author'
urlpatterns = [
    url(r'^login/', views.login_view, name='login'),
    url(r'^register/', views.register_view, name='register'),
    url(r'^logout/', views.logout_view, name='logout'),
]
