from django.db import models


class Book(models.Model):
    b_name = models.CharField(max_length=32)   # 字段名可以以表名作为前缀
    b_price = models.FloatField(default=1)


class Game(models.Model):
    g_name = models.CharField(max_length=32)
    g_price = models.FloatField(default=1)


class Movie(models.Model):
    m_name = models.CharField(max_length=32)
    m_price = models.FloatField(default=1)


class User(models.Model):
    u_name = models.CharField(max_length=32,unique=True)
    u_password = models.CharField(max_length=100)
