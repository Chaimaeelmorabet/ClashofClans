from django.conf.urls import patterns, include, url
from ClashofClans.views import mainpage
from django.contrib import admin
admin.autodiscover()



urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    (r'^ClashofClans/',  include('ClashofClans.urls',  namespace='ClashofClans')),

    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^accounts/login/$', 'django.contrib.auth.views.login'),
    url(r'^accounts/logout/$', 'django.contrib.auth.views.logout'),

)
