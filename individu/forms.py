from django import forms
from .models import Individu
from .models import Groupe

class IndividuForm(forms.ModelForm):        #formulaire pour modifier ou ajouter un individu

    class Meta:
        model = Individu                        #utiliser le model Individu
        fields = ('NOM', 'PRENOM', 'EMAIL', 'NUM', 'ANNUAIRE', 'GROUPE', 'STATUT')


class GroupeForm(forms.ModelForm):        #formulaire pour modifier ou ajouter un groupe

    class Meta:
        model = Groupe                        #utiliser le model Individu
        fields = ('ANNEE', 'FILIERE', 'NOM')