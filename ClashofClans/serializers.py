from django.contrib.auth.models import User, Group
from ClashofClans.models import Ciutat,Clan,Guerra,Jugador,Lligue,PremiLligue
from rest_framework import serializers
from rest_framework.fields import CharField


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')

class CiutatSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Ciutat
        fields = ('id',)
        fields = ( 'jugador',)
        jugador = CharField(read_only=True)

class ClanSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Clan
        fields = ('id',)
        '''fields = ( 'jugador',)
        jugador = CharField(read_only=True)'''

class GuerraSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Guerra
        fields = ('id',)
        '''fields = ( 'jugador',)
        jugador = CharField(read_only=True)'''

class JugadorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Jugador
        fields = ('id',)
        '''fields = ( 'jugador',)
        jugador = CharField(read_only=True)'''

class LligueSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Lligue
        fields = ('id',)
        '''fields = ( 'jugador',)
        jugador = CharField(read_only=True)'''

class PremiLligueSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PremiLligue
        fields = ('id',)
        '''fields = ( 'jugador',)
        jugador = CharField(read_only=True)'''