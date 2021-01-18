from django.contrib import admin
from .models import Individu
from .models import Groupe
from .models import Statut

#pour faire afficher les tables dans l'administrateur
admin.site.register(Individu)
admin.site.register(Groupe)
admin.site.register(Statut)