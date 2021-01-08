from django.shortcuts import render
from .models import Individu
from django.shortcuts import render, get_object_or_404

# Create your views here.

def individu_list(request):
    individus= Individu.objects.all()
    return render(request, 'home/individu_list.html', {'individus': individus})

def Action(request, pk):
    individu = get_object_or_404(Individu, pk=pk)
    return render(request, 'home/Action.html', {'individu': individu})
