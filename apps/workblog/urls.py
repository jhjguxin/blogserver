from django.conf.urls.defaults import *
from django.views.generic.simple import direct_to_template

urlpatterns = patterns('',
#        url(r'^map/(?P<path>.*)$', 'django.views.static.serve', {'document_root': 'map'}),
      url(r"^$",direct_to_template,{'template':'workblog/workblog.html'},name='workblog'), 
      url(r"^blog",direct_to_template,{'template':'workblog/blog'},name='blog'),    
    )

