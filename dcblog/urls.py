"""dcblog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from article import views

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^$', views.index, name='index'),
    url(r'^about/', views.about_view, name='about'),
    url(r'^article/', include('article.urls'), name='article'),
    url(r'^tag/', include('tag.urls'), name='tag'),
    url(r'^author/', include('author.urls'), name='author'),
]

urlpatterns += staticfiles_urlpatterns()
handler404 = 'dcblog.views.page404'
handler500 = 'dcblog.views.page500'
