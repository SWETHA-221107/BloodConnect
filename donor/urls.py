from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register_donor, name='register_donor'),
    path('donors/', views.find_donors, name='find_donors'),
    path('request/', views.blood_request, name='blood_request'),
]