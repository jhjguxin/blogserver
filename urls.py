from django.conf.urls.defaults import *
from django.contrib import admin
from django.views.generic.simple import direct_to_template
from blogserver.views import *
from django.views.static import serve
from django.contrib.auth.views import login,logout
admin.autodiscover()
import os, sys

static = os.path.join(
    os.path.dirname(__file__), 'static'
)

urlpatterns = patterns('',
    (r'^edit/', include('blogserver.apps.blog.urls.edit')),
#    (r'^api/', include('blogserver.api.urls')),
    (r'^admin/', include(admin.site.urls)),
    (r'^admin/doc/', include('django.contrib.admindocs.urls')),
#    (r'^admin/(.*)', admin.site.root),
    (r'^base$', base_page),
#    (r'^static/css/(?P<path>.*)$', 'django.views.static.serve', {'document_root': '/home/jhjguxin/Desktop/djcode/blogserver/static/css'}),
#    (r'^static/img/(?P<path>.*)$', 'django.views.static.serve', {'document_root': '/home/jhjguxin/Desktop/djcode/blogserver/static/img'}),

    # Blog
    (r'^', include('apps.blog.urls.posts')),
    # Categories
    (r'^categories/', include('apps.blog.urls.categories')),
    
    # Tag
    (r'^tag/', include('apps.blog.urls.tags')),
    # Comments
    (r'^comments/', include('django.contrib.comments.urls')),
    # about
    (r'^about/', include('apps.about.urls')),

)

from django.conf import settings
if settings.DEBUG:
    urlpatterns += patterns('',
	    # Images, Css, etc...
	    (r'static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': static }),
	    (r'media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': '/usr/lib/pymodules/python2.6/django/contrib/admin/media' }),
    )
