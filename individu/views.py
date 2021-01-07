from django.shortcuts import render
from .models import Individu

# Create your views here.

def individu_list(request):
    individus= Individu.objects.all()
    return render(request, 'home/individu_list.html', {'individus':individus})
