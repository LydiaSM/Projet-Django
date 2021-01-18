from django import forms
from .models import Individu

class IndividuForm(forms.ModelForm):        #formulaire

    class Meta:
        model = Individu                        #utiliser le model Individu
        fields = ('NOM', 'PRENOM', 'EMAIL', 'NUM', 'ANNUAIRE', 'GROUPE', 'STATUT')