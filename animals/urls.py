
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='animals_home'),
    path('info/', views.info, name='animals_info'),
    path('contact/', views.contact, name='animals_contact'),
]
