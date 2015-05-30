# Create your views here.

from django.template.loader import get_template

from rest_framework import viewsets
from rest_framework import permissions
from django.template import Context
from django.contrib.auth import logout

from django.core import serializers
from django.contrib.auth.decorators import login_required
from django.core import urlresolvers
from django.core.exceptions import PermissionDenied
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import get_object_or_404
from django.utils.decorators import method_decorator
from django.views.generic import DetailView, ListView, DeleteView
from django.views.generic.base import TemplateResponseMixin
from django.views.generic.edit import CreateView, UpdateView

from models import Ciutat,Clan,Guerra,Jugador,Lligue,PremiLligue
from forms import CiutatForm,JugadorForm, ClanForm, GuerraClanForm, LligaForm, PremiLligaForm
from ClashofClans import serializer

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

class LoginRequiredMixin(object):
    """Ensures that user must be authenticated in order to access view."""
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(LoginRequiredMixin, self).dispatch(*args, **kwargs)

class CheckIsOwnerMixin(object):
    def get_object(self, *args, **kwargs):
        obj = super(CheckIsOwnerMixin, self).get_object(*args, **kwargs)
        if not obj.user == self.request.user:
            raise PermissionDenied
        return obj

def logout_page(request):
    logout(request)
    return HttpResponseRedirect('/')

def mainpage(request):
    template = get_template('ClashofClans/main.html')
    variables = Context({
    'titlehead': 'Clash Of Clans',
    'user': request.user,
    })
    output = template.render(variables)
    return HttpResponse(output)

class CiutatDetail(DetailView, ConnegResponseMixin):
    model = Ciutat
    template_name = 'ClashofClans/ciutat_detail.html'

    def get_context_data(self, **kwargs):
        context = super(CiutatDetail, self).get_context_data(**kwargs)
        return context


class CiutatDelete(LoginRequiredMixin,DeleteView):
    model = Ciutat
    template_name = 'ClashofClans/delete.html'
    success_url = '/ClashofClans/ciutats/'

class CiutatCreate(LoginRequiredMixin, CreateView):
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


class JugadorDetail(DetailView, ConnegResponseMixin):
    model = Jugador
    template_name = 'ClashofClans/jugador_detail.html'

    def get_context_data(self, **kwargs):
        context = super(JugadorDetail, self).get_context_data(**kwargs)
        return context

class JugadorDelete(LoginRequiredMixin,DeleteView):
    model = Jugador
    template_name = 'ClashofClans/delete.html'
    template = get_template(template_name)
    variables = Context({
    'titlehead': 'Delete Jugador',
    })
    output = template.render(variables)
    HttpResponse(output)
    success_url = '/ClashofClans/jugadors/'

class JugadorCreate(LoginRequiredMixin, CreateView):
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


class ClanDetail(DetailView, ConnegResponseMixin):
    model = Clan
    template_name = 'ClashofClans/clan_detail.html'

    def get_context_data(self, **kwargs):
        context = super(ClanDetail, self).get_context_data(**kwargs)
        return context

class ClanDelete(LoginRequiredMixin,DeleteView):
    model = Clan
    template_name = 'ClashofClans/delete.html'
    success_url = '/ClashofClans/clans/'

class ClanCreate(LoginRequiredMixin, CreateView):
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

class GuerraClanDetail(DetailView, ConnegResponseMixin):
    model = Guerra
    template_name = 'ClashofClans/guerraClan_detail.html'

    def get_context_data(self, **kwargs):
        context = super(GuerraClanDetail, self).get_context_data(**kwargs)
        return context


class GuerraDelete(LoginRequiredMixin,DeleteView):
    model = Guerra
    template_name = 'ClashofClans/delete.html'
    success_url = '/ClashofClans/guerres/'

class GuerraClanCreate(LoginRequiredMixin, CreateView):
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

class LligaDetail(DetailView, ConnegResponseMixin):
    model = Lligue
    template_name = 'ClashofClans/lliga_detail.html'

    def get_context_data(self, **kwargs):
        context = super(LligaDetail, self).get_context_data(**kwargs)
        return context


class LligaDelete(LoginRequiredMixin,DeleteView):
    model = Lligue
    template_name = 'ClashofClans/delete.html'
    success_url = '/ClashofClans/lligues/'

class LligaCreate(LoginRequiredMixin, CreateView):
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

class PremiLligaDetail(DetailView, ConnegResponseMixin):
    model = PremiLligue
    template_name = 'ClashofClans/premiLliga_detail.html'

    def get_context_data(self, **kwargs):
        context = super(PremiLligaDetail, self).get_context_data(**kwargs)
        return context


class PremiLligaDelete(LoginRequiredMixin,DeleteView):
    model = PremiLligue
    template_name = 'ClashofClans/delete.html'
    success_url = '/ClashofClans/premis/'

class PremiLligaCreate(LoginRequiredMixin, CreateView):
    model = PremiLligue
    template_name = 'ClashofClans/form.html'
    form_class = PremiLligaForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(PremiLligaCreate, self).form_valid(form)

class PremiList(ListView, ConnegResponseMixin):
    model = PremiLligue
    queryset=PremiLligue.objects.all()
    context_object_name='latest_premi_list'
    template_name='ClashofClans/premiLligues_list.html'

#View Set FRAMEWORK

class CiutatViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Ciutat.objects.all()
    serializer_class = serializer.CiutatSerializer

class ClanViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Clan.objects.all()
    serializer_class = serializer.ClanSerializer

class GuerraViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Guerra.objects.all()
    serializer_class = serializer.GuerraSerializer

class JugadorViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Jugador.objects.all()
    serializer_class = serializer.JugadorSerializer

class LligueViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Lligue.objects.all()
    serializer_class = serializer.LligueSerializer

class PremiLligueViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = PremiLligue.objects.all()
    serializer_class = serializer.PremiLligueSerializer

#RESTful API views

class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True
        # Instance must have an attribute named `owner`.
        return obj.user == request.user


class CheckIsOwnerMixin(object):
    def get_object(self, *args, **kwargs):
        obj = super(CheckIsOwnerMixin, self).get_object(*args, **kwargs)
        if not obj.user == self.request.user:
            raise PermissionDenied
        return obj