import os
from django.db import models
from django.core import validators
# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    thumbnail = models.FileField(upload_to='files',validators=[validators.FileExtensionValidator(['jpg','png','gid'],message="必须是上述格式文件图片")])
    # thumbnail = models.ImageField(upload_to='files')
    # thumbnail = models.ImageField(upload_to='%Y%m%d')
