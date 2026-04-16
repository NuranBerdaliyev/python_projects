from django.shortcuts import render
from django.http import HttpResponse
from firstapp.models import Boxer

def boxer(request):
    return HttpResponse("Boxer")

def ladies_and_gentlemen(request):
    return render(request, 'first/firstexample.html', {'boxers': Boxer.objects.all()})

def details(request, id_thisboxer):
    return render(request, 'first/details.html', 
                  {'thisboxer': Boxer.objects.get(id=id_thisboxer)})
