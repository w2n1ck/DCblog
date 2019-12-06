# -*- coding: utf-8 -*-
'''
-----------------------------------
    FileName:     tools
    Description:  
    Author:       瓦都尅
    Date:         2019/11/20
-----------------------------------
'''
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
import functools


def login_denied(fun):
    @functools.wraps(fun)
    def wrapper(request):
        if request.user.is_authenticated:
            return HttpResponseRedirect(reverse_lazy('index'))
        return fun(request)
    return wrapper