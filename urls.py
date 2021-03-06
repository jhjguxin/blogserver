from django.conf.urls.defaults import *
from django.contrib import admin
from django.views.generic.simple import direct_to_template
from blogserver.views import *
from django.views.static import serve
from django.contrib.auth.views import login,logout
admin.autodiscover()
from django.contrib.sitemaps import FlatPageSitemap, GenericSitemap
from blogserver.apps.blog.models import Post
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
#    (r'^calendar$', post_calendar),
#    (r'^static/css/(?P<path>.*)$', 'django.views.static.serve', {'document_root': '/home/jhjguxin/Desktop/djcode/blogserver/static/css'}),
#    (r'^static/img/(?P<path>.*)$', 'django.views.static.serve', {'document_root': '/home/jhjguxin/Desktop/djcode/blogserver/static/img'}),

    # Blog
    (r'^', include('blogserver.apps.blog.urls.posts')),
    # Categories
    (r'^categories/', include('blogserver.apps.blog.urls.categories')),
    
    # Tag
    (r'^tag/', include('blogserver.apps.blog.urls.tags')),
    # Comments
    (r'^comments/', include('django.contrib.comments.urls')),
    # about
    (r'^about/', include('blogserver.apps.about.urls')),

    (r'^git/', include('blogserver.apps.git.urls')),

    (r'^workblog/', include('blogserver.apps.workblog.urls')),
)

from django.conf import settings
if settings.DEBUG:
    urlpatterns += patterns('',
	    # Images, Css, etc...
	    (r'static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': static }),
	    (r'media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': '/usr/lib/pymodules/python2.6/django/contrib/admin/media' }),
    )

info_dict = {
    'queryset': Post.objects.all(),
    'date_field': 'date_published',
}

sitemaps = {
    'flatpages': FlatPageSitemap,
    'blog': GenericSitemap(info_dict, priority=0.6),
}

urlpatterns += patterns('',
    # some generic view using info_dict
    # ...

    # the sitemap
    (r'^sitemap\.xml$', 'django.contrib.sitemaps.views.sitemap', {'sitemaps': sitemaps})
)
urlpatterns += patterns('django.contrib.sitemaps.views',
    (r'^sitemap\.xml$', 'index', {'sitemaps': sitemaps}),
    (r'^sitemap-(?P<section>.+)\.xml$', 'sitemap', {'sitemaps': sitemaps}),
)
