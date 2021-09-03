from django.shortcuts import render
from .models import Ngo
from django.shortcuts import get_object_or_404

# Create your views here.

def ngo(request):
    ngo = Ngo.objects.all()
    data = {
        'ngo': ngo,
    }
    return render(request, 'ngo/ngo.html', data)

def ngo_detail(request, id):
    ngo = get_object_or_404(Ngo, pk=id)
    data = {
        'ngo': ngo,
    }
    return render(request, 'ngo/ngo_detail.html', data)

def search(request):
    ngo = Ngo.objects.all()
    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        if keyword:
            ngo = ngo.filter(description__icontains = keyword)    


    data = {
        'ngo': ngo,
    }


    return render(request, 'ngo/search.html', data)