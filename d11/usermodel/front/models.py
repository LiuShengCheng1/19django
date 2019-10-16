# from django.db import models
# from django.contrib.auth.models import User
# from django.dispatch import receiver
# from django.db.models.signals import post_save
#
#
# # User.objects.all()
# # Person.object.all()
# # Person是user的代理，以上两个是等同的
# # 在代理模型中不能添加字段
# class Person(User):
#     class Meta:
#         proxy = True  #表明立场，我是user模型的代理模型
#
#
#         @classmethod
#         def get_black_list(cls):
#             return cls.objects.filter(is_active=False)
#
#
#
# class UserExtension(models.Model):
#     user = models.OneToOneField(User,on_delete=models.CASCADE,related_name="extension")
#     telephone = models.CharField(max_length=11)
#     school = models.CharField(max_length=100)