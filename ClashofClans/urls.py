from django.conf.urls import patterns, url, include
from django.views.generic import DetailView, ListView, UpdateView
from rest_framework import routers
from django.contrib import admin
from ClashofClans.models import Ciutat,Clan,Guerra,Jugador,Lligue,PremiLligue
from forms import CiutatForm,JugadorForm, ClanForm, GuerraClanForm, LligaForm, PremiLligaForm
from views import CiutatCreate,CiutatDetail,JugadorCreate,JugadorDetail, ClanCreate, GuerraClanCreate, LligaCreate, PremiLligaCreate, ClanDetail,\
    GuerraClanDetail, LligaDetail,PremiLligaDetail

from ClashofClans import views
admin.autodiscover()

router = routers.DefaultRouter()
router.register(r'ciutats', views.CiutatViewSet)
router.register(r'clans', views.ClanViewSet)
router.register(r'guerres', views.GuerraViewSet)
router.register(r'jugadors', views.JugadorViewSet)
router.register(r'lligues', views.LligueViewSet)
router.register(r'premilligues', views.PremiLligueViewSet)

urlpatterns = patterns('',
    url(r'^api/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^$', views.mainpage, name='home'),

    url(r'^ciutats/$', views.CiutatList.as_view(), name='ciutat_list'),
    url(r'^jugadors/$', views.JugadorList.as_view(), name='jugador_list'),
    url(r'^clans/$', views.ClanList.as_view(), name='clan_list'),
    url(r'^guerres/$', views.GuerraList.as_view(), name='guerra_list'),
    url(r'^lligues/$', views.LligaList.as_view(), name='lliga_list'),
    url(r'^premis/$', views.PremiList.as_view(), name='premi_list'),

    #  *********************    Ciutat    ************************

    # Ciutat details, ex.: /ClashofClans/ciutats/1/
    url(r'^ciutats/(?P<pk>\d+)/$', #ClashofClans/pk=1/ si posem el pk, si nomes posem el d+ ClashofClans/1/. Posar nom ens pot servir per a un futur fer distincions
        CiutatDetail.as_view(),
        name='ciutat_detail'),

    url(r'^ciutats/(?P<pk>\d+)\.(?P<extension>(json|xml))$',
        CiutatDetail.as_view(),
        name='ciutat_detail_conneg'),

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

    url(r'^jugadors/(?P<pk>\d+)\.(?P<extension>(json|xml))$',
        JugadorDetail.as_view(),
        name='jugador_detail_conneg'),

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
    url(r'^clans/(?P<pk>\d+)\.(?P<extension>(json|xml))$',
        ClanDetail.as_view(),
        name='clan_detail_conneg'),

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
    url(r'^guerraClan/(?P<pk>\d+)\.(?P<extension>(json|xml))$',
        GuerraClanDetail.as_view(),
        name='guerraClan_detail_conneg'),

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
    url(r'^lliga/(?P<pk>\d+)\.(?P<extension>(json|xml))$',
        LligaDetail.as_view(),
        name='lliga_detail_conneg'),

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
    url(r'^premiLliga/(?P<pk>\d+)\.(?P<extension>(json|xml))$',
        PremiLligaDetail.as_view(),
        name='premiLliga_detail_conneg'),


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

#urlpatterns = format_suffix_patterns(urlpatterns, allowed=['api','json', 'xml'])
#RESTful API

