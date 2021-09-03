from django.shortcuts import render
from .models import Caretaker
from django.shortcuts import get_object_or_404

# Create your views here.

def caretaker(request):
    caretaker = Caretaker.objects.all()
    data = {
        'caretaker': caretaker,
    }
    return render(request, 'caretaker/caretaker.html', data)

def caretaker_detail(request, id):
    care = get_object_or_404(Caretaker, pk=id)
    data = {
        'care': care,
    }
    return render(request, 'caretaker/caretaker_detail.html', data)

def search(request):
    caretaker = Caretaker.objects.all()
    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        if keyword:
            caretaker = caretaker.filter(description__icontains = keyword)    


    data = {
        'caretaker': caretaker,
    }

    return render(request, 'caretaker/search.html', data)
