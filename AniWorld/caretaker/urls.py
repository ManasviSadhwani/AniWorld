from django.urls import path
from . import views

urlpatterns = [
    path('', views.caretaker, name = "caretaker"),
    path('<int:id>', views.caretaker_detail, name = "caretaker_detail"),
    path('search', views.search, name = "search"),
]