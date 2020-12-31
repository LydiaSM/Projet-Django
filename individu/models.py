from django.conf import settings
from django.db import models
from django.utils import timezone


class Individu (models.Model):
    statut = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    ID = models.AutoField(primary_key=True)
    NOM = models.TextField()
    PRENOM = models.TextField()
    EMAIL = models.EmailField(max_length=254)
    NUM = models.TextField()
    ANNUAIRE = models.IntegerField()


    def ajoutgroupe(self):
        self.save()

    def __str__(self):
        return self.NOM