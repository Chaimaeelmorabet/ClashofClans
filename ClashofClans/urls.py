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
            queryset=Lligue.objects.all()[:5],
            context_object_name='latest_lligue_list',
            template_name='ClashofClans/main.html'),
        name='ciutat_list'),
    # List latest 5 ciutats: /ClashofClans/

    url(r'^ciutats/$',
        ListView.as_view(
            queryset=Ciutat.objects.all(),
            context_object_name='latest_ciutat_list',
            template_name='ClashofClans/ciutat_list.html'),
        name='ciutats_list'),

        url(r'^jugadors/$',
        ListView.as_view(
            queryset=Jugador.objects.all(),
            context_object_name='latest_jugador_list',
            template_name='ClashofClans/jugador_list.html'),
        name='jugador_list'),

        url(r'^clans/$',
        ListView.as_view(
            queryset=Clan.objects.all(),
            context_object_name='latest_clan_list',
            template_name='ClashofClans/clan_list.html'),
        name='clan_list'),

        url(r'^guerres/$',
        ListView.as_view(
            queryset=Guerra.objects.all(),
            context_object_name='latest_guerra_list',
            template_name='ClashofClans/guerra_list.html'),
        name='guerra_list'),

        url(r'^lligues/$',
        ListView.as_view(
            queryset=Lligue.objects.all(),
            context_object_name='latest_lliga_list',
            template_name='ClashofClans/lliga_list.html'),
        name='lliga_list'),

        url(r'^premis/$',
        ListView.as_view(
            queryset=PremiLligue.objects.all(),
            context_object_name='latest_premi_list',
            template_name='ClashofClans/premi_list.html'),
        name='premi_list'),



    

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

    url(r'^clan/(?P<pk>\d+)/edit/$',
        UpdateView.as_view(
            model=Clan,
            form_class=ClanForm,
            template_name='ClashofClans/form.html'),
        name='clan_edit'),

    #*****************Guerra Clan***************************

    # jugador details, ex.: /ClashofClans/jugador/1/
    url(r'^guerraClan/(?P<pk>\d+)/$', #ClashofClans/pk=1/ si posem el pk, si nomes posem el d+ ClashofClans/1/. Posar nom ens pot servir per a un futur fer distincions
        GuerraClanDetail.as_view(),
        name='guerraClan_detail'),

    # Create a clan: /ClashofClans/guerraClan/create/
    url(r'^guerraClan/create/$',
        GuerraClanCreate.as_view(),
        name='guerraclan_create'),

        # Edit jugador details, ex: /ClashofClans/jugadors/1/edit/
    url(r'^guerraClan/(?P<pk>\d+)/edit/$',
        UpdateView.as_view(
            model=Guerra,
            form_class=GuerraClanForm,
            template_name='ClashofClans/form.html'),
        name='guerraClan_edit'),

    #*****************Lliga***************************

    # jugador details, ex.: /ClashofClans/jugador/1/
    url(r'^lliga/(?P<pk>\d+)/$', #ClashofClans/pk=1/ si posem el pk, si nomes posem el d+ ClashofClans/1/. Posar nom ens pot servir per a un futur fer distincions
        LligaDetail.as_view(),
        name='lliga_detail'),

    # Create a clan: /ClashofClans/clan/create/
    url(r'^lliga/create/$',
        LligaCreate.as_view(),
        name='lliga_create'),

        # Edit jugador details, ex: /ClashofClans/jugadors/1/edit/
    url(r'^lliga/(?P<pk>\d+)/edit/$',
        UpdateView.as_view(
            model=Lligue,
            form_class=LligaForm,
            template_name='ClashofClans/form.html'),
        name='lliga_edit'),

    #*****************Premi Lliga***************************

    # jugador details, ex.: /ClashofClans/jugador/1/
    url(r'^premiLliga/(?P<pk>\d+)/$', #ClashofClans/pk=1/ si posem el pk, si nomes posem el d+ ClashofClans/1/. Posar nom ens pot servir per a un futur fer distincions
        PremiLligaDetail.as_view(),
        name='premiLliga_detail'),
        # Edit jugador details, ex: /ClashofClans/jugadors/1/edit/
    url(r'^jugadors/(?P<pk>\d+)/edit/$',
        UpdateView.as_view(
            model=Jugador,
            form_class=JugadorForm,
            template_name='ClashofClans/form.html'),
        name='jugador_edit'),

    # Create a clan: /ClashofClans/clan/create/
    url(r'^premiLliga/create/$',
        PremiLligaCreate.as_view(),
        name='premi_create'),
        # Edit jugador details, ex: /ClashofClans/jugadors/1/edit/
    url(r'^premiLliga/(?P<pk>\d+)/edit/$',
        UpdateView.as_view(
            model=PremiLligue,
            form_class=PremiLligaForm,
            template_name='ClashofClans/form.html'),
        name='premiLliga_edit'),

)
