from django.urls import path

from . import views

urlpatterns = [
    path('contactadmin/', views.contactadmin, name="contactadmin"),
]