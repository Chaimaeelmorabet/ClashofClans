from django.contrib.auth.models import User, Group
from ClashofClans.models import Ciutat,Clan,Guerra,Jugador,Lligue,PremiLligue
from rest_framework import serializers
from rest_framework.fields import CharField
from rest_framework.relations import HyperlinkedRelatedField, HyperlinkedIdentityField
from rest_framework.serializers import HyperlinkedModelSerializer

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('name')

class CiutatSerializer(serializers.HyperlinkedModelSerializer):
    jugador = CharField(read_only=True)

    class Meta:
        model = Ciutat
        fields = ('id','jugador')


class ClanSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Clan
        fields = ('nom', 'id', 'punts', 'tipus', 'trofeusBase', 'ubicacio')

class GuerraSerializer(serializers.HyperlinkedModelSerializer):
    clan1 = CharField(read_only=True)
    clan2 = CharField(read_only=True)
    class Meta:
        model = Guerra
        fields = ('id', 'clan1', 'clan2')

class JugadorSerializer(serializers.HyperlinkedModelSerializer):
    clan = CharField(read_only=True)

    class Meta:
        model = Jugador
        fields = ('nom', 'id', 'nivell', 'lliga', 'clan')

class LligueSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Lligue
        fields = ('id', 'premi', 'numCopes')

class PremiLligueSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PremiLligue
        fields = ('id', 'nom', 'oro', 'elixir', 'elixirNegre')