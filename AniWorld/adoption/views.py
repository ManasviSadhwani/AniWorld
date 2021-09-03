from django.shortcuts import render
from .models import Adoption
from django.shortcuts import get_object_or_404

# Create your views here.

def adoption(request):
    adoption = Adoption.objects.all()
    data = {
        'adoption': adoption,
    }
    return render(request, 'adoption/adoption.html', data)

def adoption_detail(request, id):
    adopt = get_object_or_404(Adoption, pk=id)
    data = {
        'adopt': adopt,
    }

    return render(request, 'adoption/adoption_detail.html', data)

def search(request):

    adoption = Adoption.objects.all()
    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        if keyword:
            adoption = adoption.filter(description__icontains = keyword)    


    data = {
        'adoption': adoption,
    }

    return render(request, 'adoption/search.html')

