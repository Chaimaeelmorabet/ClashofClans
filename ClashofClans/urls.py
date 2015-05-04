from django.conf.urls import patterns, url
from django.utils import timezone
from django.views.generic import DetailView, ListView, UpdateView

from ClashofClans.models import Ciutat,Clan,Guerra,Jugador,Lligue,PremiLligue
from forms import CiutatForm,JugadorForm, ClanForm, GuerraClanForm, LligaForm, PremiLligaForm
from views import CiutatCreate,CiutatDetail,JugadorCreate,JugadorDetail, ClanCreate, GuerraClanCreate, LligaCreate, PremiLligaCreate, ClanDetail,\
    GuerraClanDetail, LligaDetail,PremiLligaDetail

urlpatterns = patterns('',

    url(r'^$',
        ListView.as_view(
            queryset=Ciutat.objects.all()[:5],
            context_object_name='latest_ciutat_list',
            template_name='ClashofClans/main.html'),
        name='ciutat_list'),
    # List latest 5 ciutats: /ClashofClans/



    

    #  *********************    Ciutat    ************************

    # Ciutat details, ex.: /ClashofClans/ciutats/1/
    url(r'^ciutats/(?P<pk>\d+)/$', #ClashofClans/pk=1/ si posem el pk, si nomes posem el d+ ClashofClans/1/. Posar nom ens pot servir per a un futur fer distincions
        CiutatDetail.as_view(),
        name='ciutat_detail'),

    # Create a ciutat: /ClashofClans/ciutats/create/
    url(r'^ciutats/create/$',
        CiutatCreate.as_view(),
        name='ciutat_create'),

    # Edit ciutat details, ex: /ClashofClans/ciutats/1/edit/
    url(r'^ciutats/(?P<pk>\d+)/edit/$',
        UpdateView.as_view(
            model=Ciutat,
            form_class=CiutatForm,
            template_name='ClashofClans/form.html'),
        name='ciutat_edit'),

    #  ********************   Jugador   *********************

    # jugador details, ex.: /ClashofClans/jugador/1/
    url(r'^jugadors/(?P<pk>\d+)/$', #ClashofClans/pk=1/ si posem el pk, si nomes posem el d+ ClashofClans/1/. Posar nom ens pot servir per a un futur fer distincions
        JugadorDetail.as_view(),
        name='jugador_detail'),

    # Create a jugador: /ClashofClans/jugadors/create/
    url(r'^jugadors/create/$',
        JugadorCreate.as_view(),
        name='jugador_create'),

    # Edit jugador details, ex: /ClashofClans/jugadors/1/edit/
    url(r'^jugadors/(?P<pk>\d+)/edit/$',
        UpdateView.as_view(
            model=Jugador,
            form_class=JugadorForm,
            template_name='ClashofClans/form.html'),
        name='jugador_edit'),

    #*****************Clan***************************

    # jugador details, ex.: /ClashofClans/jugador/1/
    url(r'^clans/(?P<pk>\d+)/$', #ClashofClans/pk=1/ si posem el pk, si nomes posem el d+ ClashofClans/1/. Posar nom ens pot servir per a un futur fer distincions
        ClanDetail.as_view(),
        name='clan_detail'),

    # Create a clan: /ClashofClans/clan/create/
    url(r'^clans/create/$',
        ClanCreate.as_view(),
        name='clan_create'),

    #*****************Guerra Clan***************************
    # jugador details, ex.: /ClashofClans/jugador/1/
    url(r'^guerraClan/(?P<pk>\d+)/$', #ClashofClans/pk=1/ si posem el pk, si nomes posem el d+ ClashofClans/1/. Posar nom ens pot servir per a un futur fer distincions
        GuerraClanDetail.as_view(),
        name='guerraClan_detail'),

    # Create a clan: /ClashofClans/guerraClan/create/
    url(r'^guerraClan/create/$',
        GuerraClanCreate.as_view(),
        name='guerraclan_create'),

    #*****************Lliga***************************
    # jugador details, ex.: /ClashofClans/jugador/1/
    url(r'^lliga/(?P<pk>\d+)/$', #ClashofClans/pk=1/ si posem el pk, si nomes posem el d+ ClashofClans/1/. Posar nom ens pot servir per a un futur fer distincions
        LligaDetail.as_view(),
        name='lliga_detail'),

    # Create a clan: /ClashofClans/clan/create/
    url(r'^lliga/create/$',
        LligaCreate.as_view(),
        name='lliga_create'),

    #*****************Premi Lliga***************************
    # jugador details, ex.: /ClashofClans/jugador/1/
    url(r'^premiLliga/(?P<pk>\d+)/$', #ClashofClans/pk=1/ si posem el pk, si nomes posem el d+ ClashofClans/1/. Posar nom ens pot servir per a un futur fer distincions
        JugadorDetail.as_view(),
        name='premiLliga_detail'),

    # Create a clan: /ClashofClans/clan/create/
    url(r'^premiLliga/create/$',
        PremiLligaCreate.as_view(),
        name='premi_create'),

)
