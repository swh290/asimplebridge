from django.conf.urls import patterns, include, url
from views import *
from account.views import *
from django.conf import settings
from django.conf.urls.static import static

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'asimplebridge.views.home', name='home'),
    # url(r'^asimplebridge/', include('asimplebridge.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^$', home, name='home'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^login/', login, name='login'),
    url(r'^signup/', signup, name='signup'),
    url(r'^logout/', logout, name='logout'),
    url(r'^register/', register, name='register'),
    url(r'^fbLogin/', fbLogin, name='fbLogin'),
    url("", include('django_socketio.urls')),
    
)+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
