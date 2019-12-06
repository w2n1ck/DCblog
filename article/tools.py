# -*- coding: utf-8 -*-
'''
-----------------------------------
    FileName:     tools
    Description:  
    Author:       瓦都尅
    Date:         2019/11/16
-----------------------------------
'''
from django.conf import settings


def get_field_attrs(placeholder, textarea=False):
    ret = {
        'class': 'form-control',
        'placeholder': placeholder
    }
    if textarea:
        ret.update({'row': 20})
    return ret


def delete_no_article_tag(tags):
    for t in tags:
        if not t.article_set.count():
            t.delete()
