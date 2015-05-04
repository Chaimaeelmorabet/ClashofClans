from django.forms import ModelForm
from ClashofClans.models import Ciutat,Clan,Guerra,Jugador,Lligue,PremiLligue

class CiutatForm(ModelForm):
    class Meta:
        model = Ciutat
        exclude = ('user', 'date',)

class JugadorForm(ModelForm):
    class Meta:
        model = Jugador
        exclude = ('user', 'date',)

class ClanForm(ModelForm):
    class Meta:
        model = Clan
        exclude = ('user', 'date',)

class GuerraClanForm(ModelForm):
    class Meta:
        model = Guerra
        exclude = ('user', 'date',)

class LligaForm(ModelForm):
    class Meta:
        model = Lligue
        exclude = ('user', 'date',)

class PremiLligaForm(ModelForm):
    class Meta:
        model = PremiLligue
        exclude = ('user', 'date',)


