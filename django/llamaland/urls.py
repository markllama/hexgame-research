from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

from llamaland.hexgame.views import GameListView, MapListView

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'llamaland.views.home', name='home'),
    # url(r'^llamaland/', include('llamaland.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

    # hexgame view pattern.
    url(r'^games/$', GameListView.as_view()),
    url(r'^maps/$', MapListView.as_view()),
)
