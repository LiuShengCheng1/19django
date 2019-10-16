from . import views
from django.urls import path

urlpatterns = [
    path('',views.book),
    path('detail/<int:book_id>/',views.book_detail),
    path('detail/<str:book_id>/',views.book_detail),
    path('detail/<uuid:book_id>/',views.book_detail),
    path('list/',views.book_list)
]