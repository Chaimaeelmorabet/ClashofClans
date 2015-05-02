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
            queryset=Ciutat.objects.filter(date__lte=timezone.now()).order_by('date')[:5],
            context_object_name='latest_ciutat_list',
            template_name='ClashofClans/restaurant_list.html'),
        name='restaurant_list'),


    # Restaurant details, ex.: /myrestaurants/restaurants/1/
    url(r'^ClashofClans/(?P<pk>\d+)/$', #myrestaurants/pk=1/ si posem el pk, si nomes posem el d+ myrestaurants/1/. Posar nom ens pot servir per a un futur fer distincions
        CiutatDetail.as_view(),
        name='ciutat_detail'),

    # Create a restaurant: /myrestaurants/restaurants/create/
    url(r'^ClashofClans/create/$',
        CiutatCreate.as_view(),
        name='ciutat_create'),

    # Edit restaurant details, ex: /myrestaurants/restaurants/1/edit/
    url(r'^ClashofClans/(?P<pk>\d+)/edit/$',
        UpdateView.as_view(
            model=Ciutat,
            form_class=CiutatForm,
            template_name='ClashofClans/form.html'),
        name='ciutat_edit'),

   ''' # Restaurant dish details, ex: /myrestaurants/restaurants/1/dishes/1/
    url(r'^restaurants/(?P<pkr>\d+)/dishes/(?P<pk>\d+)/$',
        DetailView.as_view(
            model=Dish,
            template_name='myrestaurants/dish_detail.html'),
        name='dish_detail'),

    # Create a restaurant dish, ex: /myrestaurants/restaurants/1/dishes/create/
    url(r'^restaurants/(?P<pk>\d+)/dishes/create/$',
        DishCreate.as_view(),
        name='dish_create'),

    # Edit restaurant dish details, ex: /myrestaurants/restaurants/1/dishes/1/edit/
    url(r'^restaurants/(?P<pkr>\d+)/dishes/(?P<pk>\d+)/edit/$',
        UpdateView.as_view(
            model=Dish,
            form_class=DishForm,
            template_name='myrestaurants/form.html'),
        name='dish_edit'),

    # Create a restaurant review using function, ex: /myrestaurants/restaurants/1/reviews/create/
    url(r'^restaurants/(?P<pk>\d+)/reviews/create/$',
        'myrestaurants.views.review',
        name='review_create')''',
)
