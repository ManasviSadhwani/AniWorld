from django.urls import path
from . import views

urlpatterns = [
    path('', views.ngo, name = "ngo"),
    path('<int:id>', views.ngo_detail, name = "ngo_detail"),
    path('search', views.search, name = "search"),
]