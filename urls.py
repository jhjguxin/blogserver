from django.conf.urls.defaults import *
from django.contrib import admin
from django.views.generic.simple import direct_to_template
from blogserver.views import *
from django.views.static import serve
admin.autodiscover()
import os, sys

site_media = os.path.join(
    os.path.dirname(__file__), 'static'
)

urlpatterns = patterns('',
    (r'^edit/', include('blogserver.apps.blog.urls.edit')),
#    (r'^api/', include('blogserver.api.urls')),
    (r'^admin/', include(admin.site.urls)),
#    (r'^admin/(.*)', admin.site.root),
    (r'^base$', base_page),
    (r'^static/css/(?P<path>.*)$', 'django.views.static.serve', {'document_root': '/home/jhjguxin/Desktop/djcode/blogserver/static/css'}),
    (r'^static/img/(?P<path>.*)$', 'django.views.static.serve', {'document_root': '/home/jhjguxin/Desktop/djcode/blogserver/static/img'}),

    # Blog
    (r'^', include('apps.blog.urls.posts')),
    # Categories
    (r'^categories/', include('apps.blog.urls.categories')),
    
    # Tag
    (r'^tag/', include('apps.blog.urls.tags')),


)
