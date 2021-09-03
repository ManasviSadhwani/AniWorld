from django.shortcuts import render
from .models import Slider
from adoption.models import Adoption
from caretaker.models import Caretaker
from ngo.models import Ngo
from vets.models import Vets

# Create your views here.

def home(request):
    sliders = Slider.objects.all()
    adoption = Adoption.objects.order_by('-created_date')
    caretaker = Caretaker.objects.order_by('-created_date')
    ngo = Ngo.objects.order_by('-created_date')
    vets = Vets.objects.order_by('-created_date')


    data = {
        'sliders' : sliders,
        'adoption' : adoption,
        'caretaker' : caretaker,
        'ngo' : ngo,
        'vets' : vets
    }

    return render(request, 'webpages/home.html', data)


def about(request):
    return render(request, 'webpages/about.html')


def contact(request):
    return render(request, 'webpages/contact.html')