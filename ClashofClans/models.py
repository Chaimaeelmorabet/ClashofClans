# -*- coding: utf-8 -*-
from django.db import models
from django_countries.fields import CountryField

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

class Jugador(models.Model):
    nom = models.CharField(max_length=60)
    id = models.IntegerField();
    nivell= models.IntegerField(default=0);
    idLliga = models.IntegerField(default=0)
    idCiutat = models.IntegerField()
    idClan = models.IntegerField(default=0)

class Lliga(models.Model):
    idLliga = models.IntegerField(default=0)
    idPremi = models.IntegerField(default=0)
    numCopes = models.IntegerField(default=0);

class Guerra(models.Model):
    idGuerra = models.IntegerField()
    idClan1 = models.IntegerField()
    idClan2 = models.IntegerField()

class Ciutat(models.Model):
    id = models.IntegerField()

class PremiLliga(models.Model):
    id = models.IntegerField()
    oro = models.IntegerField()
    elixir = models.IntegerField()
    elixirNegre = models.IntegerField()
