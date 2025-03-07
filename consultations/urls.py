from django.urls import path
from . import views

urlpatterns = [
    path('book/', views.book_consultation, name='book_consultation'),
    path('list/', views.booking_list, name='booking_list'),
]
