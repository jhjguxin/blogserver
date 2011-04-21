from django.conf.urls.defaults import *
from django.views.generic.simple import direct_to_template

urlpatterns = patterns('',
#        url(r'^map/(?P<path>.*)$', 'django.views.static.serve', {'document_root': 'map'}),
      url(r"^$",direct_to_template,{'template':'about/Personal_Details.html'},name='about_html'),
      url(r"^$",direct_to_template,{'template':'about/Personal_Details.txt'},name='about_md'),
    )

