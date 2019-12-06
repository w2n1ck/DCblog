from django.db import models


# Create your models here.


class Tag(models.Model):
    name = models.CharField(max_length=20, unique=True, verbose_name="标签名")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "标签"
        verbose_name_plural = verbose_name