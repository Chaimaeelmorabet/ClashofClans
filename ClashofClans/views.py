# Create your views here.
from django.views.generic import DetailView

from django.views.generic.edit import CreateView
from ClashofClans.serializers import CiutatSerializer
from rest_framework import viewsets

from models import Ciutat,Clan,Guerra,Jugador,Lligue,PremiLligue
from forms import CiutatForm,JugadorForm, ClanForm, GuerraClanForm, LligaForm, PremiLligaForm


class CiutatDetail(DetailView):
    model = Ciutat
    template_name = 'ClashofClans/ciutat_detail.html'

    def get_context_data(self, **kwargs):
        context = super(CiutatDetail, self).get_context_data(**kwargs)
        return context

class CiutatCreate(CreateView):
    model = Ciutat
    template_name = 'ClashofClans/form.html'
    form_class = CiutatForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(CiutatCreate, self).form_valid(form)

class JugadorDetail(DetailView):
    model = Jugador
    template_name = 'ClashofClans/jugador_detail.html'

    def get_context_data(self, **kwargs):
        context = super(JugadorDetail, self).get_context_data(**kwargs)
        return context

class JugadorCreate(CreateView):
    model = Jugador
    template_name = 'ClashofClans/form.html'
    form_class = JugadorForm


    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(JugadorCreate, self).form_valid(form)


class ClanDetail(DetailView):
    model = Clan
    template_name = 'ClashofClans/clan_detail.html'

    def get_context_data(self, **kwargs):
        context = super(ClanDetail, self).get_context_data(**kwargs)
        return context

class ClanCreate(CreateView):
    model = Clan
    template_name = 'ClashofClans/form.html'
    form_class = ClanForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(ClanCreate, self).form_valid(form)

class GuerraClanDetail(DetailView):
    model = Guerra
    template_name = 'ClashofClans/guerraClan_detail.html'

    def get_context_data(self, **kwargs):
        context = super(GuerraClanDetail, self).get_context_data(**kwargs)
        return context

class GuerraClanCreate(CreateView):
    model = Guerra
    template_name = 'ClashofClans/form.html'
    form_class = GuerraClanForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(GuerraClanCreate, self).form_valid(form)

class LligaDetail(DetailView):
    model = Lligue
    template_name = 'ClashofClans/lliga_detail.html'

    def get_context_data(self, **kwargs):
        context = super(LligaDetail, self).get_context_data(**kwargs)
        return context

class LligaCreate(CreateView):
    model = Lligue
    template_name = 'ClashofClans/form.html'
    form_class = LligaForm

    def form_valid(self, form):
        form.instance.user = self.request.user

        return super(LligaCreate, self).form_valid(form)

class PremiLligaDetail(DetailView):
    model = PremiLligue
    template_name = 'ClashofClans/premiLliga_detail.html'

    def get_context_data(self, **kwargs):
        context = super(PremiLligaDetail, self).get_context_data(**kwargs)
        return context

class PremiLligaCreate(CreateView):
    model = PremiLligue
    template_name = 'ClashofClans/form.html'
    form_class = PremiLligaForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(PremiLligaCreate, self).form_valid(form)

class CiutatViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Ciutat.objects.all()
    serializer_class = CiutatSerializer