from django.urls import path
from . import views #must import views because that contains the functions 

urlpatterns = [
    path('', views.mumbai,name='mumbai'),
    path('mumbai_book', views.mumbai_book,name='mumbai_book'),
    path('payment',views.payment,name='payment'),
    path('viewbooking',views.viewbooking,name='viewbooking')
]