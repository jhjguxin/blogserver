from django.conf.urls.defaults import *
#from blogserver.apps.blog.models import Tag
from taggit.models import Tag
from blogserver.apps.blog.models import Post

display_dict = {
    'queryset' : Post.live.all(),
    'template_name' : 'blog/tag_detail.html',
}

#urlpatterns = patterns('blogserver.taggit.views',
urlpatterns = patterns('taggit.views',    
    # Display Post in Category
    url(r'^(?P<slug>[-\w]+)/$', 'tagged_object_list', display_dict, name="tag_detail"),
    
)
