from django.conf import settings
from django.db import models
from django.utils import timezone


class Groupe (models.Model):                    #creation de la table Groupe
    statut = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    ID = models.AutoField(primary_key=True)
    ANNEE = models.IntegerField()
    FILIERE = models.CharField(max_length= 20)
    NOM = models.CharField(max_length=20)

    def publish(self):
        self.save()

    def __str__(self):
        return self.FILIERE + ' ' + self.NOM


class Statut (models.Model):                    #creation de la table Statut
    statut = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    ID = models.AutoField(primary_key=True)
    NOM = models.CharField(max_length=20)

    def publish(self):
        self.save()

    def __str__(self):
        return self.NOM


class Individu (models.Model):                      #creation de la table Individu
    statut = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    ID = models.AutoField(primary_key=True)
    NOM = models.CharField(max_length=30)
    PRENOM = models.CharField(max_length=20)
    EMAIL = models.EmailField(max_length=50)
    NUM = models.CharField(max_length=20)
    ANNUAIRE = models.IntegerField()

    GROUPE = models.CharField(max_length=20, default='null')
    STATUT = models.CharField(max_length=20, default='null')

    def publish(self):
        self.save()

    def __str__(self):
        return self.NOM + ' ' + self.PRENOM


