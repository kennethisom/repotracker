from django.conf.urls import patterns, include, url
from django.contrib import admin
import accounts

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'repotracker.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', 'repos.views.index', name='home'),
    url(r'^accounts/', include('accounts.urls', namespace='accounts', app_name='accounts')),
    url(r'^admin/', include(admin.site.urls)),
)
