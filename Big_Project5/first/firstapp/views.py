from django.shortcuts import render
from django.http import HttpResponse
from firstapp.models import Boxer

def boxer(request):
    return HttpResponse("Boxer")

def ladies_and_gentlemen(request):
    boxers = Boxer.objects.all()
    average_hp=0
    for boxer in boxers:
        average_hp+=boxer.hp
    average_hp=average_hp/len(boxers)
    return render(request, 'first/firstexample.html', {'boxers': boxers, 
                                                       'average_hp': average_hp})

def details(request, id_thisboxer):
    return render(request, 'first/details.html', 
                  {'boxer': Boxer.objects.get(id=id_thisboxer)})

def all_details(request):
    return render(request, 'first/alldetails.html', {'boxers': Boxer.objects.all()})

def home(request):
    return render(request, 'first/main.html')

def ifelse(request, id_thisboxer):
    boxer=Boxer.objects.get(id=id_thisboxer)
    return render(request, 'first/ifelseincluding.html', {'bx': boxer})
