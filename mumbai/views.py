from django.shortcuts import render, redirect, HttpResponse
from mumbai.models import PassengerDetails
from django.contrib import messages

# Create your views here.
def mumbai(request):
    return render(request,'Mumbai.html')

def mumbai_book(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        age = request.POST['age']
        date = request.POST['date']
        ins = PassengerDetails(first_name=first_name, last_name=last_name, email=email, age=age, date=date)
        ins.save()
        messages.info(request,'Added passenger details! You may add more passengers.')
    return render(request,'mumbai_book.html')

def payment(request):
    return render(request,'payment.html')

def viewbooking(request):
    passengers = PassengerDetails.objects.all()
    return render(request,'viewbooking.html', {'passengers' : passengers})