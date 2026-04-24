from django.urls import path
from django.template import loader
from . import views

urlpatterns=[
    path('', views.home, name='main'),
    path('boxerlist/', views.ladies_and_gentlemen, name='boxerlist'),
    path('boxerlist/alldetails/', views.all_details, name='all_details'),
    path('boxerlist/details/<int:id_thisboxer>/', views.details, name='details'),
    path('boxer_test/', views.boxer, name='boxer'),
    path('boxerlist/ifelse/<int:id_thisboxer>/', views.ifelse, name='ifelse'),
]