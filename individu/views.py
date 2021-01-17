from django.shortcuts import redirect
from django.shortcuts import render
from .models import Individu
from django.shortcuts import render, get_object_or_404
from .forms import IndividuForm                 #acces au formulaire du nv individu


# Create your views here.

def individu_list(request):
    individus= Individu.objects.all()           #publier tt les individus
    return render(request, 'home/individu_list.html', {'individus': individus})

def Detail(request, pk):
    individu = get_object_or_404(Individu, pk=pk)
    return render(request, 'home/Detail.html', {'individu': individu})

def NVindividu(request):
    if request.method == "POST":                #qd on saisie des données
        form = IndividuForm(request.POST)
        if form.is_valid():                     #verifie que les champs sont corrects et non vides
            individu = form.save(commit=False)
            individu.author = request.user
            individu.save()
            return redirect('Detail', pk=individu.pk)
    else:
        form = IndividuForm()
    return render(request, 'home/ModifIndividu.html', {'form': form})

def ModifIndividu(request, pk):
    individu = get_object_or_404(Individu, pk=pk)
    if request.method == "POST":
        form = IndividuForm(request.POST, instance=individu)
        if form.is_valid():
            individu = form.save(commit=False)
            individu.author = request.user
            individu.save()
            return redirect('Detail', pk=individu.pk)
    else:
        form = IndividuForm(instance=individu)
    return render(request, 'home/ModifIndividu.html', {'form': form})



