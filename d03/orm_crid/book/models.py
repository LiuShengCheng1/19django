from django.db import models


# Create your models here.

class Book(models.Model):
    name = models.CharField(max_length=50, null=False)
    author = models.CharField(max_length=50, null=False)
    prize = models.FloatField(default=0)

    def __str__(self):
        return "<Book:({name},{author},{prize})>".format(name=self.name, author=self.author, prize=self.prize)
