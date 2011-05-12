from django.conf.urls.defaults import *
from django.views.generic.simple import direct_to_template

urlpatterns = patterns('',
#        url(r'^map/(?P<path>.*)$', 'django.views.static.serve', {'document_root': 'map'}),
      url(r"^$",direct_to_template,{'template':'git/git.html'},name='git'),      
    )

