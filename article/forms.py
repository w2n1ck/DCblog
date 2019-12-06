# -*- coding: utf-8 -*-
'''
-----------------------------------
    FileName:     forms
    Description:  
    Author:       瓦都尅
    Date:         2019/11/16
-----------------------------------
'''
from django import forms
from django.conf import settings

from .tools import get_field_attrs, delete_no_article_tag
from .models import Article
from tag.models import Tag


class MyTagField(forms.Field):
    widget = forms.TextInput(get_field_attrs('Tags'))

    def clean(self, value):
        return value


class ArticleForm(forms.ModelForm):
    tag_list = MyTagField(required=False)

    class Meta:
        model = Article
        fields = ('title', 'background', 'tag_list', 'content')
        widgets = {
            'title': forms.TextInput(get_field_attrs('标题')),
            'background': forms.TextInput(get_field_attrs('背景URL, 默认 {}'.format(settings.DCBLOG_CONFIG.get('SITE_ARTICLE_BACKGROUND')))),
            'content': forms.Textarea(get_field_attrs('markdown正文', textarea=True))
        }

    def __init__(self, *args, **kwargs):
        super(ArticleForm, self).__init__(*args, **kwargs)
        self.initial['tag_list'] = ','.join([
            t.name for t in Tag.objects.filter(article=self.instance).all()
        ])
        self.fields['background'].required = False

    def clean_tag_list(self):
        tags = self.cleaned_data.get('tag_list') or []
        if tags:
            if ' ' in tags:
                raise forms.ValidationError('多个标签使用,号分割')
            return tags.split(',')
        return tags

    def save(self, commit=True):
        article = super(ArticleForm, self).save()
        tags = self.cleaned_data.get('tag_list')
        if tags:
            remove_tags = [t for t in article.tag.all() if t.name not in tags]
            article.tag.remove(*remove_tags)
            delete_no_article_tag(remove_tags)

            for item in tags:
                tag = Tag.objects.filter(name=item).first()
                if not tag:
                    tag = Tag.objects.create(name=item)
                article.tag.add(tag)
        else:
            remove_tags = article.tag.all()
            article.tag.remove(*remove_tags)
            delete_no_article_tag(remove_tags)
        return article