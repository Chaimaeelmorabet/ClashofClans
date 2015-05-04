from django.conf.urls import patterns, url
from django.utils import timezone
from django.views.generic import DetailView, ListView, UpdateView

from ClashofClans.models import Ciutat,Clan,Guerra,Jugador,Lligue,PremiLligue
from forms import CiutatForm
from views import CiutatCreate,CiutatDetail

urlpatterns = patterns('',
    # List latest 5 restaurants: /myrestaurants/
    url(r'^$',
        ListView.as_view(
            queryset=Ciutat.objects.all(),
            context_object_name='latest_ciutat_list',
            template_name='ClashofClans/main.html'),
        name='ciutat_list'),
    # Create a restaurant: /ClashofClans/ciutats/create/
    url(r'^ciutats/create/$',
        CiutatCreate.as_view(),
        name='ciutat_create'),


)
