# from rest_framework.authentication import BaseAuthentication
# from django.core.cache import cache
# from .models import User
#
#
# class UserAuthentication(BaseAuthentication):
#     def authenticate(self, request):
#         try:
#             token = request.query_pasamms.get('token')
#             user_id = cache.get(token)
#
#             user = User.objects.get(pk=user_id)
#             return user,token
#
#         except Exception as e:
#             return None