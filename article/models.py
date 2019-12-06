from django.db import models
from django.contrib.auth.models import User
from django.utils.html import strip_tags
from mistune import markdown
from django.urls import reverse


from tag.models import Tag


# Create your models here.


class Article(models.Model):
    title = models.CharField(max_length=100, verbose_name="标题")
    description = models.CharField(max_length=200, null=True, verbose_name="摘要")
    background = models.CharField(max_length=500, null=True, verbose_name="背景图片")
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="作者")
    content = models.TextField(blank=True, verbose_name="正文")
    tag = models.ManyToManyField(Tag, verbose_name="标签")
    read_num = models.IntegerField(default=1000, verbose_name="阅读量")
    pub_date = models.DateTimeField(editable=False, auto_now_add=True, verbose_name="发表时间")

    def save(self, *args, **kwargs):
        # md = markdown.Markdown(extensions=[
        #     'markdown.extensions.extra',
        #     'markdown.extensions.codehilite',
        # ])
        self.description = strip_tags(markdown(self.content))[:80]

        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('article:detail', kwargs={'pk': self.pk})

    @property
    def render_content(self):
        return markdown(self.content)

    @property
    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "文章列表"
        verbose_name_plural = verbose_name
        ordering = ['-pub_date']
