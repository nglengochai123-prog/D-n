from django.urls import path , re_path
from . import views
urlpatterns = [
 path('books/', views.book_list, name='book_list'),
 path('books/<int:id>/', views.book_detail, name='book_detail')
]

