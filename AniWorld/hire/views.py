from django.shortcuts import render, redirect
from .models import Hire
from django.contrib import messages

# Create your views here.


   
def hire(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        adopt_id = request.POST['adopt_id']
        
        city = request.POST['city']
        phone = request.POST['phone']
        email = request.POST['email']
        state = request.POST['state']
        message = request.POST['message']
        user_id = request.POST['user_id']


        #todo: do all sanitization

        hire = Hire(first_name=first_name, last_name=last_name, adopt_id=adopt_id, city=city, phone=phone, email=email, state=state, message=message, user_id=user_id)
        hire.save()
        messages.success(request, 'Thanks for reaching out!')
        return redirect('adoption')

