# -*- coding: utf-8 -*-
from django.db import models
from django_countries.fields import CountryField
from django.core.urlresolvers import reverse

# Create your models here.
class Clan(models.Model):
    tipusOpciones = ((1,'Privado'),(2,'Publico'),(3,'Solo invitacion'))
    nom = models.CharField(max_length=60)
    idClan = models.AutoField(primary_key=True)
    punts = models.IntegerField(default=0)
    tipus = models.PositiveSmallIntegerField('Tipo clan', blank=False, default=2, choices=tipusOpciones)
    trofeusBase = models.IntegerField(default=0)
    ubicacio = CountryField()
    def __unicode__(self):
        return self.nom
    def get_absolute_url(self):
        return reverse('ClashofClans:ciutat_list', kwargs={})

class PremiLligue(models.Model):
    id = models.AutoField(primary_key=True)
    oro = models.IntegerField()
    elixir = models.IntegerField()
    elixirNegre = models.IntegerField()
    def __unicode__(self):
        return str(self.id)
    def get_absolute_url(self):
        return reverse('ClashofClans:ciutat_list', kwargs={})

class Lligue(models.Model):
    idLliga = models.AutoField(primary_key=True)
    idPremi = models.ForeignKey(PremiLligue, null=True)
    numCopes = models.IntegerField(default=0)
    def __unicode__(self):
        return str(self.idLliga)
    def get_absolute_url(self):
        return reverse('ClashofClans:ciutat_list', kwargs={})

class Jugador(models.Model):
    nom = models.CharField(max_length=60)
    id = models.AutoField(primary_key=True)
    nivell= models.IntegerField(default=0)
    lliga = models.ForeignKey(Lligue, null=True,blank=True)
    clan = models.ForeignKey(Clan, null=True,blank=True)
    def __unicode__(self):
        return self.nom
    def get_absolute_url(self):
        return reverse('ClashofClans:ciutat_list', kwargs={})

class Guerra(models.Model):
    idGuerra = models.AutoField(primary_key=True)
    idClan1 = models.ForeignKey(Clan, null=True, related_name='idClans1')
    idClan2 = models.ForeignKey(Clan, null=True, related_name='idClans2')
    def __unicode__(self):
        str(self.idGuerra)
    def get_absolute_url(self):
        return reverse('ClashofClans:ciutat_list', kwargs={})


class Ciutat(models.Model):
    id = models.AutoField(primary_key=True)
    jugador = models.ForeignKey(Jugador, null=True, related_name='ciutats')

    def __unicode__(self):
        return str(self.id)
    def get_absolute_url(self):
        return reverse('ClashofClans:ciutat_list', kwargs={})


