# -*- coding: utf-8 -*-
'''
-----------------------------------
    FileName:     views
    Description:  
    Author:       瓦都尅
    Date:         2019/11/20
-----------------------------------
'''
from django.shortcuts import render_to_response
from django.template import RequestContext


def page404(request, exception):
    response = render_to_response('error.html', {
        'status_code': 404,
        'message': '你来到了没有知识的荒原 :('
    })
    response.status_code = 404
    return response


def page500(request):
    response = render_to_response('error.html', {
        'status_code': 500,
        'message': '你来到了没有知识的荒原 :('
    })
    response.status_code = 500
    return response