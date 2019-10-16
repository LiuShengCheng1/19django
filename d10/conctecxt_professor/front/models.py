from django.db import models
from django.core.validators import MaxValueValidator,MinLengthValidator

class User(models.Model):
    username = models.CharField(max_length=100,validators=[MinLengthValidator(6,message="用户名最短不能少于6位")])
    password = models.CharField(max_length=30,validators=[MinLengthValidator(6,message="密码最短不能少于6位")])
    telephone = models.CharField(max_length=11)
    pub_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'user_model'
        ordering = ['-pub_date']
