from django.urls import path
from django.template import loader
from . import views

urlpatterns=[
    path('boxer/', views.boxer, name='boxer'),
    path('boxerlist/', views.ladies_and_gentlemen, name='boxerlist'),
    path('boxerlist/details/<int:id_thisboxer>/', views.details, name='details')
]