# Create your views here.

from django.core import urlresolvers
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.views.generic import DetailView
from django.views.generic.edit import CreateView

from models import Ciutat,Clan,Guerra,Jugador,Lligue,PremiLligue
from forms import CiutatForm

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