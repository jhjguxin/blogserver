from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.utils.translation import ugettext as _
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.core.urlresolvers import reverse
#from blogserver.apps.blog.models import Posts

from dynamicresponse.response import *

from forms import *
from models import *

from django.views.decorators.csrf import csrf_exempt
import pdb

"""
def posts(request):
    posts = Posts.objects.all()

    return render_to_response("posts.html", {
        'posts': posts },
        RequestContext(request))
    
def test_js(request):
    return render_to_response('test_js.html', {}, RequestContext(request))
"""
@ csrf_exempt
def post_index(request):
  """Lists all blog post."""
    
  if request.method == 'POST':
    post = Post.objects.create(title=request.POST.get("title"), reviewer=request.POST.get("reviewer"), email=request.POST.get("email"),content=request.POST.get("content") )
    post.save()
    form = PostsForm(request.POST, instance=post)
    #posts = Posts.objects.all()
  else:
    form = PostsForm(instance=None)
  posts = Post.objects.all()
  #pdb.set_trace()
  return SerializeOrRender('blog/post_index.html', { 'posts': posts }, extra={ 'form': form })

def posts_list(request):
    """Lists all blog post."""
    
    posts = Post.objects.all()
    return SerializeOrRender('blog/posts_list.html', { 'posts': posts })

    
def post_delete(request, post_id):
    """Deletes the blog post."""
    
    post = get_object_or_404(Post.objects.all(), pk=post_id)
    
    if request.method == 'POST':

        post.delete()
        return SerializeOrRedirect(reverse('posts_list'), {}, status=CR_DELETED)
    
    else:
        
        return SerializeOrRender('blog/post_delete.html', { 'post': post }, status=CR_CONFIRM)

def post(request, post_id=None):
    """Displays, creates or updates a blog posts."""
    
    post = None
    if post_id:
        post = get_object_or_404(Post.objects.all(), pk=post_id)

    if request.method == 'POST':
        
        form = PostsForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save()
            return SerializeOrRedirect(reverse('posts_list'), { 'post': post })
            
    else:
        
        form = PostsForm(instance=post)
    
    return SerializeOrRender('blog/post.html', { 'post': post }, extra={ 'form': form })

