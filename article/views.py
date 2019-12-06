from django.shortcuts import render, get_object_or_404, render_to_response
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.http import HttpResponseForbidden, HttpResponseRedirect
import markdown

from .models import Article
from .forms import ArticleForm
from django.conf import settings


# Create your views here.


def index(request):
    paginator = Paginator(Article.objects.all(), 10)
    page = request.GET.get('page')
    try:
        articles = paginator.page(page)
    except PageNotAnInteger:
        articles = paginator.page(1)
    except EmptyPage:
        articles = paginator.page(paginator.num_pages)
    return render(request, 'home.html', context={
        'articles': articles
    })


def detail(requests, article_id):
    article = get_object_or_404(Article, pk=article_id)
    # article.content = markdown.markdown(article.content, extensions=[
    #     'markdown.extensions.extra',
    #     'markdown.extensions.codehilite',
    #     'markdown.extensions.toc'
    # ])
    tags = article.tag.all()
    return render(requests, 'article_detail.html', context={
        'article': article,
        'tags': tags
    })


@login_required(login_url=reverse_lazy('author:login'))
def edit(request, article_id):
    article = get_object_or_404(Article, pk=article_id)
    if article.author != request.user and request.user.is_superuser:
        return HttpResponseForbidden(render_to_response('error.html', {
            'status_code': 403,
            'message': 'Forbidden :('
        }))
    form = ArticleForm(request.POST or None, instance=article)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse_lazy('article:detail', kwargs={
            'article_id': form.instance.id
        }))
    context={
        'form': form,
        'header_id': 'tag-heading',
        'title': '编辑文章',
        'subtitle': form.instance.title,
        'background': form.instance.background or settings.DCBLOG_CONFIG.get('SITE_ARTICLE_BACKGROUND'),
        'submit': '保存编辑'
    }
    return render(request, 'generic_form.html', context=context)


@login_required(login_url=reverse_lazy('author:login'))
def add(request):
    form = ArticleForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.instance.author = request.user
        form.save()
        return HttpResponseRedirect(reverse_lazy('article:detail', kwargs={
            'article_id': form.instance.id
        }))
    context = {
        'form': form,
        'header_id': 'tag-heading',
        'title': '添加文章',
        'subtitle': '文章标题',
        'background': form.instance.background or settings.DCBLOG_CONFIG.get('SITE_ARTICLE_BACKGROUND'),
        'submit': '添加'
    }
    return render(request, 'generic_form.html', context=context)


def about_view(request):
    return render(request, 'about.html')