from django.shortcuts import render
from .models import Vets
from django.shortcuts import get_object_or_404

# Create your views here.

def vets(request):
    vets = Vets.objects.all()
    data = {
        'vets': vets,
    }
    return render(request, 'vets/vets.html', data)

def vets_detail(request, id):
    vets = get_object_or_404(Vets, pk=id)
    data = {
        'vets': vets,
    }
    return render(request, 'vets/vets_detail.html', data)

def search(request):
    vets = Vets.objects.all()
    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        if keyword:
            vets = vets.filter(description__icontains = keyword)    


    data = {
        'vets': vets,
    }

    return render(request, 'vets/search.html', data)