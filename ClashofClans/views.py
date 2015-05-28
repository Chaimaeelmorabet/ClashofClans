# Create your views here.
from django.views.generic import DetailView
from django.template.loader import get_template
from django.views.generic.edit import CreateView
from ClashofClans import serializers
from rest_framework import viewsets
from rest_framework import generics, permissions
from django.template import Context
from django.core import serializers
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.core import urlresolvers
from django.core.exceptions import PermissionDenied
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import get_object_or_404
from django.utils.decorators import method_decorator
from django.views.generic import DetailView, ListView, TemplateView
from django.views.generic.base import TemplateResponseMixin
from django.views.generic.edit import CreateView, UpdateView

from models import Ciutat,Clan,Guerra,Jugador,Lligue,PremiLligue
from forms import CiutatForm,JugadorForm, ClanForm, GuerraClanForm, LligaForm, PremiLligaForm
from ClashofClans import serializers

class ConnegResponseMixin(TemplateResponseMixin):
    def render_json_object_response(self, objects, **kwargs):
        json_data = serializers.serialize(u"json", objects, **kwargs)
        return HttpResponse(json_data, content_type=u"application/json")
    def render_xml_object_response(self, objects, **kwargs):
        xml_data = serializers.serialize(u"xml", objects, **kwargs)
        return HttpResponse(xml_data, content_type=u"application/xml")
    def render_to_response(self, context, **kwargs):
        if 'extension' in self.kwargs:
            try:
                objects = [self.object]
            except AttributeError:
                objects = self.object_list
            if self.kwargs['extension'] == 'json':
                return self.render_json_object_response(objects=objects)
            elif self.kwargs['extension'] == 'xml':
                return self.render_xml_object_response(objects=objects)
        else:
            return super(ConnegResponseMixin, self).render_to_response(context)

def mainpage(request):
    template = get_template('ClashofClans/main.html')
    variables = Context({
    'titlehead': 'Clash Of Clans',
    'user': request.user,
    })
    output = template.render(variables)
    return HttpResponse(output)

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


class CiutatList(ListView, ConnegResponseMixin):
    model= Ciutat
    queryset=Ciutat.objects.all()
    context_object_name='latest_ciutat_list'
    template_name='ClashofClans/ciutat_list.html'


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

class JugadorList(ListView, ConnegResponseMixin):
    model= Jugador
    queryset=Jugador.objects.all()
    context_object_name='latest_jugador_list'
    template_name='ClashofClans/jugador_list.html'


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


class ClanList(ListView, ConnegResponseMixin):
    model= Clan
    queryset=Clan.objects.all()
    context_object_name='latest_clan_list'
    template_name='ClashofClans/clan_list.html'

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

class GuerraList(ListView, ConnegResponseMixin):
    model = Guerra
    queryset=Guerra.objects.all()
    context_object_name='latest_guerra_list'
    template_name='ClashofClans/guerra_list.html'

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

class LligaList(ListView, ConnegResponseMixin):
    model = Lligue
    queryset=Lligue.objects.all()
    context_object_name='latest_lliga_list'
    template_name='ClashofClans/lliga_list.html'

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

class PremiList(ListView, ConnegResponseMixin):
    queryset=PremiLligue.objects.all()
    context_object_name='latest_premi_list'
    template_name='ClashofClans/premi_list.html'

#View Set FRAMEWORK

class CiutatViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Ciutat.objects.all()
    serializer_class = serializers.CiutatSerializer

class ClanViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Clan.objects.all()
    serializer_class = serializers.ClanSerializer

class GuerraViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Guerra.objects.all()
    serializer_class = serializers.GuerraSerializer

class JugadorViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Jugador.objects.all()
    serializer_class = serializers.JugadorSerializer

class LligueViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Lligue.objects.all()
    serializer_class = serializers.LligueSerializer

class PremiLligueViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = PremiLligue.objects.all()
    serializer_class = serializers.PremiLligue

#RESTful API views

class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True
        # Instance must have an attribute named `owner`.
        return obj.user == request.user