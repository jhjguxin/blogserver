from django.conf.urls.defaults import *
from blogserver.apps.blog.models import Category

display_dict = {
    'queryset' : Category.objects.all(),
}

urlpatterns = patterns('django.views.generic.list_detail',
    
    # Display Post in Category
    url(r'^(?P<slug>[-\w]+)/$', 'object_detail', display_dict, name="category_detail"),
    
)



