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