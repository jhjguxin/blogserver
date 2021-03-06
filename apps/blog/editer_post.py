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
@login_required
def post_index(request, post_id=None):
    """Displays, creates or updates a blog posts."""
    
    post = None
    posts = Post.objects.all()
    if request.method == 'POST':
        
        form = PostsForm(request.POST, instance=post)
        if form.is_valid():
            #pdb.set_trace()
            instance = form.save(commit=False)
            instance.author = request.user
            instance.save() 


        return SerializeOrRedirect(reverse('post_index'), { 'posts': posts })
            
    else:
        
        form = PostsForm(instance=post)
    
#        return SerializeOrRender('blog/post_edit.html', { 'post': post }, extra={ 'form': form })
        return SerializeOrRender('blog/post_index.html', { 'posts': posts }, extra={ 'form': form })

@login_required
def posts_list(request):
    """Lists all blog post."""
    
    posts = Post.objects.all()
    return SerializeOrRender('blog/posts_list.html', { 'posts': posts })

@login_required    
def post_delete(request, post_id):
    """Deletes the blog post."""
    ok=False    
    post = get_object_or_404(Post.objects.all(), pk=post_id)
    if post.author.username==request.user.username:
#        pdb.set_trace()
        ok=True
        if request.method == 'POST':
         
            post.delete()
            return SerializeOrRedirect(reverse('posts_list'), {}, status=CR_DELETED)
    
    
    return SerializeOrRender('blog/post_delete.html', { 'post': post,'ok':ok }, status=CR_CONFIRM)
@login_required
def post(request, post_id=None):
    """Displays, creates or updates a blog posts."""
    
    post = None
    edit=False
    if post_id:
        post = get_object_or_404(Post.objects.all(), pk=post_id)
        edit=True
        

    if request.method == 'POST':
        
        form = PostsForm(request.POST, instance=post)
        if edit:
            #pdb.set_trace()
            form.save()
            instance = form.instance
            instance.author = request.user
            instance.save() 
        else:
            if form.is_valid():
                #pdb.set_trace()
                ct=form.cleaned_data
                instance = form.save(commit=False)
                instance.author = request.user
                instance.save() 
        posts = Post.objects.all()
        return SerializeOrRedirect(reverse('posts_list'), { 'posts': posts })
            
    else:
        
        form = PostsForm(instance=post)
    
        return SerializeOrRender('blog/post_edit.html', { 'post': post }, extra={ 'form': form })

