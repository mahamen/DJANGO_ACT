
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='shoe_brands_home'),
    path('info/', views.info, name='shoe_brands_info'),
    path('contact/', views.contact, name='shoe_brands_contact'),
]
