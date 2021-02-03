from django.shortcuts import redirect
from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from .models import Individu
from .forms import IndividuForm                 #acces au formulaire du nv individu
from .models import Groupe
from .forms import GroupeForm                   #acces au formulaire du nv groupe

#permet de connecter les models et les pages html, les templates

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
            individu.statut = request.user
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
            individu.statut = request.user
            individu.save()
            return redirect('Detail', pk=individu.pk)
    else:
        form = IndividuForm(instance=individu)
    return render(request, 'home/ModifIndividu.html', {'form': form})



def groupe_list(request):
    groupes= Groupe.objects.all()
    return render(request, 'home/groupe_list.html', {'groupes': groupes})

def groupe_detail(request, pk):
    groupe = get_object_or_404(Groupe, pk=pk)
    return render(request, 'home/groupe_detail.html', {'groupe': groupe})

def NVgroupe(request):
    if request.method == "POST":                #qd on saisie des données
        form = GroupeForm(request.POST)
        if form.is_valid():                     #verifie que les champs sont corrects et non vides
            groupe = form.save(commit=False)
            groupe.statut = request.user
            groupe.save()
            return redirect('groupe_detail', pk=groupe.pk)
    else:
        form = GroupeForm()
    return render(request, 'home/ModifGroupe.html', {'form': form})

def ModifGroupe(request, pk):
    groupe = get_object_or_404(Groupe, pk=pk)
    if request.method == "POST":
        form = GroupeForm(request.POST, instance=groupe)
        if form.is_valid():
            groupe = form.save(commit=False)
            groupe.statut = request.user
            groupe.save()
            return redirect('groupe_detail', pk=groupe.pk)
    else:
        form = GroupeForm(instance=groupe)
    return render(request, 'home/ModifGroupe.html', {'form': form})



def accueil(request):
    return render(request, 'home/Accueil.html', {})




