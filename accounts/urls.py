

from django.urls import path
from . import views #must import views because that contains the functions 

urlpatterns = [
    path('register', views.register,name='register'),
    path('login', views.login, name='login'),
    path('logout',views.logout, name='logout')
]