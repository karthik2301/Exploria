#urls inside the app1 gives routing for the views inside app1

from django.urls import path
from . import views #must import views because that contains the functions 

urlpatterns = [
    path('', views.index,name='index')
]