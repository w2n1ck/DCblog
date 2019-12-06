# -*- coding: utf-8 -*-
'''
-----------------------------------
    FileName:     context_processors
    Description:  
    Author:       瓦都尅
    Date:         2019/11/20
-----------------------------------
'''
from django.conf import settings

def site_info(request):
    return settings.DCBLOG_CONFIG