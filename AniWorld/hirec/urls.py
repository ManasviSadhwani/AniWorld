from django.urls import path

from . import views

urlpatterns = [
    path('hirec', views.hirec, name="hirec"),
]