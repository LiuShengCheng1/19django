from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    # 将字段设置为创建的时间，以后修改时，字段的值不会再更新。
    create_time = models.DateTimeField(auto_now_add="True")
