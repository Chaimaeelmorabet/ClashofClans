from django.forms import ModelForm
from ClashofClans.models import Ciutat,Clan,Guerra,Jugador,Lligue,PremiLligue

class CiutatForm(ModelForm):
    class Meta:
        model = Ciutat
        exclude = ('user', 'date',)


