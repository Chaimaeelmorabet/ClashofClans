# -*- coding: utf-8 -*-
from django.db import models
from django_countries.fields import CountryField
from django.core.urlresolvers import reverse

# Create your models here.
class Clan(models.Model):
    tipusOpciones = ((1,'Privado'),(2,'Publico'),(3,'Solo invitacion'))
    nom = models.CharField(max_length=60)
    idClan = models.AutoField(primary_key=True)
    idGuerra = models.IntegerField()
    punts = models.IntegerField(default=0)
    tipus = models.PositiveSmallIntegerField('Tipo clan', blank=False, default=2, choices=tipusOpciones)
    trofeusBase = models.IntegerField(default=0)
    ubicacio = CountryField()
    def __unicode__(self):
        return self.nom


class Ciutat(models.Model):
    id = models.IntegerField(primary_key=True)
    def __unicode__(self):
        return str(self.id)
    def get_absolute_url(self):
        return reverse('ClashofClans:ciutat_list', kwargs={})

class Jugador(models.Model):
    nom = models.CharField(max_length=60)
    id = models.AutoField(primary_key=True)
    nivell= models.IntegerField(default=0)
    idLliga = models.IntegerField(default=0)
    idClan = models.IntegerField(default=0)
    idCiutat = models.IntegerField()
    def __unicode__(self):
        return self.nom
    def get_absolute_url(self):
        return reverse('ClashofClans:ciutat_list', kwargs={})


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




class PremiLligue(models.Model):
    id = models.IntegerField(primary_key=True)
    oro = models.IntegerField()
    elixir = models.IntegerField()
    elixirNegre = models.IntegerField()
    def __unicode__(self):
        return str(self.id)
