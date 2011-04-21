from django.conf.urls.defaults import *
from django.contrib.auth.views import login,logout
"""
urlpatterns = patterns('blogserver.apps.blog.views',
    url(r'^$', 'posts', name='posts'),
    url(r'^js$', 'test_js'),
)
"""

urlpatterns= patterns('blogserver.apps.blog.editer_post',
    url(r'^post_index$', 'post_index', name='post_index'),
    
    url(r'^posts_show/$', 'posts_list', name='posts_list'),
    url(r'^post_create/$', 'post', name='post_create'),
    url(r'^post=(?P<post_id>\d+)/$', 'post', name='post'),
    url(r'^post=(?P<post_id>\d+)/delete/$', 'post_delete', name='post_delete'),
)
urlpatterns += patterns('blogserver.apps.blog.editer_user',
#    url(r'^index_user$', 'index_user', name='index_user'),
    
    url(r'^users_show/$', 'users_list', name='users_list'),
    url(r'^register/$', 'register', name='user_create'),
    url(r'^user=(?P<user_id>\d+)/passwordchange/$', 'passwordchange', name='passwordchange'),
    url(r'^user=(?P<user_id>\d+)/userchange/$', 'u_change', name='u_change'),
#    url(r'^user=(?P<user_id>\d+)/delete/$', 'delete_user', name='delete_user'),

)
urlpatterns += patterns('',
    url(r'^login',login,{"template_name":'blog/login.html'},name='login'),
    url(r'^logout/$', logout,{"template_name":'blog/logout.html'},name='logout'),


)

