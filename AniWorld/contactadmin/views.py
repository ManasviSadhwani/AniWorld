from .models import Contactadmin
from django.shortcuts import render, redirect
from django.contrib import messages, auth

# Create your views here.

def contactadmin(request):
    if request.method == 'POST':
        name = request.POST['name']
        number = request.POST['number']
        email = request.POST['email']
        service = request.POST['service']
        subject = request.POST['subject']
        message = request.POST['message']

        contactadmin = Contactadmin(name=name, number=number, email=email, service=service, subject=subject, message=message)
        contactadmin.save()
        messages.success(request, 'Thanks for reaching out!')
        return redirect('')