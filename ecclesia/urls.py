from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    # (r'^ecclesia/', include('ecclesia.foo.urls')),

    (r'^goal/(?P<goal_id>\d+)/visualize/$', 'ecclesia.goals.views.visualize'),
    (r'^goal/(?P<goal_id>\d+)/json/$', 'ecclesia.goals.views.json'),
    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^admin/(.*)', admin.site.root),

)
