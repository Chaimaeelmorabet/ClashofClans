# -*- coding: utf-8 -*-
from django.db import models
from django_countries.fields import CountryField
from datetime import date

# Create your models here.
class Clan(models.Model):
    tipusOpciones = ((1,'Privado'),(2,'Publico'),(3,'Solo invitacion'))
    ubicacioOpciones = ((1,'Internacional'),(2,'España'),(3,'Marruecos'))
    nom = models.CharField(max_length=60)
    idClan = models.IntegerField()
    idGuerra = models.IntegerField()
    punts = models.IntegerField(default=0)
    tipus = models.PositiveSmallIntegerField('Tipo clan', blank=False, default=2, choices=tipusOpciones)
    trofeusBase = models.IntegerField(default=0)
    ubicacio = models.IntegerField('Ubicacion', blank=False,default=1,choices=ubicacioOpciones)
    country = CountryField()
    def __unicode__(self):
        return self.nom

class Jugador(models.Model):
    nom = models.CharField(max_length=60)
    id = models.IntegerField(primary_key=True);
    nivell= models.IntegerField(default=0);
    idLliga = models.IntegerField(default=0)
    idCiutat = models.IntegerField()
    idClan = models.IntegerField(default=0)
    def __unicode__(self):
        return self.nom

class Lligue(models.Model):
    idLliga = models.IntegerField(default=0)
    idPremi = models.IntegerField(default=0)
    numCopes = models.IntegerField(default=0);
    def __unicode__(self):
        return str(self.idLliga)

class Guerra(models.Model):
    idGuerra = models.IntegerField()
    idClan1 = models.IntegerField()
    idClan2 = models.IntegerField()
    def __unicode__(self):
        str(self.idGuerra)

class Ciutat(models.Model):
    id = models.IntegerField(primary_key=True)
    def __unicode__(self):
        return str(self.id)

class PremiLligue(models.Model):
    id = models.IntegerField(primary_key=True)
    oro = models.IntegerField()
    elixir = models.IntegerField()
    elixirNegre = models.IntegerField()
    def __unicode__(self):
        return str(self.id)
