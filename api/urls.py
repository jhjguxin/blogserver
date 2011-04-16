from django.conf.urls.defaults import *
from piston.resource import Resource
from piston.authentication import HttpBasicAuthentication
from piston.doc import documentation_view

from blogserver.api.handlers import PostHandler, AddPostHandler

#auth = HttpBasicAuthentication(realm='My sample API')

#blogposts = Resource(handler=PostHandler, authentication=auth)
blogposts = Resource(handler=PostHandler)
addblogposts = Resource(handler=AddPostHandler)

urlpatterns = patterns('',
    url(r'^posts/$', blogposts),
    url(r'^posts/show$', blogposts),
    url(r'^posts/add$', addblogposts),
    # automated documentation
    url(r'^$', documentation_view),
)
