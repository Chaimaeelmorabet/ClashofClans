from django.conf.urls import patterns, include, url
from rest_framework import routers
from ClashofClans import views
from django.contrib import admin
admin.autodiscover()

router = routers.DefaultRouter()
router.register(r'ciutats', views.CiutatViewSet)

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'ClashofClansSettings.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^', include(router.urls)),
    url(r'^admin/', include(admin.site.urls)),
    (r'^ClashofClans/',  include('ClashofClans.urls',  namespace='ClashofClans')),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
)
