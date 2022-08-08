from django.shortcuts import render
from django.http import HttpResponse
from .models import destination #importing class destination

# Create your views here.

def index(request):  

    dests = destination.objects.all() #fetches data from database
    return render(request,'index.html', { 'dests': dests}) #creating key which we will use in html files
