from django.urls import path
from . import views

urlpatterns = [
    path('', views.vets, name = "vets"),
    path('<int:id>', views.vets_detail, name = "vets_detail"),
    path('search', views.search, name = "search"),
]