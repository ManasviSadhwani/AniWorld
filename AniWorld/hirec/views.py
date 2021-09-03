from django.shortcuts import render, redirect
from .models import Hirec
from django.contrib import messages

# Create your views here.


   
def hirec(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        care_id = request.POST['care_id']
        
        city = request.POST['city']
        phone = request.POST['phone']
        email = request.POST['email']
        state = request.POST['state']
        message = request.POST['message']
        user_id = request.POST['user_id']


        #todo: do all sanitization

        hirec = Hirec(first_name=first_name, last_name=last_name, care_id=care_id, city=city, phone=phone, email=email, state=state, message=message, user_id=user_id)
        hirec.save()
        messages.success(request, 'Thanks for reaching out!')
        return redirect('caretaker')

