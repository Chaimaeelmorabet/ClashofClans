
from django.contrib.auth.models import User, Group
from ClashofClans.models import Ciutat,Clan,Guerra,Jugador,Lligue,PremiLligue
from rest_framework import serializers
from rest_framework.fields import CharField
from rest_framework.relations import HyperlinkedRelatedField, HyperlinkedIdentityField


class CiutatSerializer(serializers.HyperlinkedModelSerializer):
    jugador = HyperlinkedRelatedField(read_only=True, view_name='ClashofClans:jugador_detail')
    user = CharField(read_only=True)

    class Meta:
        model = Ciutat
        fields = ('id','jugador', 'user')


class ClanSerializer(serializers.HyperlinkedModelSerializer):
    user = CharField(read_only=True)
    class Meta:
        model = Clan
        fields = ('nom', 'id', 'punts', 'tipus', 'trofeusBase', 'ubicacio', 'user')

class GuerraSerializer(serializers.HyperlinkedModelSerializer):
    clan1 = HyperlinkedIdentityField(read_only=True, view_name='ClashofClans:clan_detail')
    clan2 = HyperlinkedRelatedField(read_only=True, view_name='ClashofClans:clan_detail')
    user = CharField(read_only=True)
    class Meta:
        model = Guerra
        fields = ('id', 'clan1', 'clan2', 'user')

class JugadorSerializer(serializers.HyperlinkedModelSerializer):
    clan = HyperlinkedRelatedField(read_only=True, view_name='ClashofClans:clan_detail')
    lliga = HyperlinkedRelatedField(read_only=True, view_name='ClashofClans:lliga_detail')
    user = CharField(read_only=True)
    class Meta:
        model = Jugador
        fields = ('nom', 'localitzacio', 'id', 'nivell', 'lliga', 'clan', 'user')

class LligueSerializer(serializers.HyperlinkedModelSerializer):
    premi = HyperlinkedRelatedField(read_only=True, view_name='ClashofClans:premiLliga_detail')
    user = CharField(read_only=True)
    class Meta:
        model = Lligue
        fields = ('id', 'premi', 'numCopes')

class PremiLligueSerializer(serializers.HyperlinkedModelSerializer):
    user = CharField(read_only=True)
    class Meta:
        model = PremiLligue
        fields = ('id', 'nom', 'oro', 'elixir', 'elixirNegre', 'user')