from django.urls import path
from . import views

urlpatterns = [
    path('', views.adoption, name = "adoption"),
    path('<int:id>', views.adoption_detail, name = "adoption_detail"),
    path('adoption/search', views.search, name = "search"),
]