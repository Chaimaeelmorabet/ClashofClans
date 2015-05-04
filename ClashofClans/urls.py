from django.conf.urls import patterns, url
from django.utils import timezone
from django.views.generic import DetailView, ListView, UpdateView

from ClashofClans.models import Ciutat,Clan,Guerra,Jugador,Lligue,PremiLligue
from forms import CiutatForm
from views import CiutatCreate,CiutatDetail

urlpatterns = patterns('',
    # List latest 5 ciutats: /ClashofClans/
    url(r'^$',
        ListView.as_view(
            queryset=Ciutat.objects.all()[:5],
            context_object_name='latest_ciutat_list',
            template_name='ClashofClans/main.html'),
        name='ciutat_list'),
    

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



)
