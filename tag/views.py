from django.shortcuts import render

# Create your views here.

from .models import Tag


def tag_index(request):
    tags = Tag.objects.all()
    return render(request, 'tag.html', {'tags': tags})