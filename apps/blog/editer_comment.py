from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.utils.translation import ugettext as _
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.core.urlresolvers import reverse
#from blogserver.apps.blog.models import Comments

from dynamicresponse.response import *

from forms import *
from models import *

from django.views.decorators.csrf import csrf_exempt
import pdb

"""
def posts(request):
    posts = Comments.objects.all()

    return render_to_response("posts.html", {
        'posts': posts },
        RequestContext(request))
    
def test_js(request):
    return render_to_response('test_js.html', {}, RequestContext(request))
"""
@ csrf_exempt
def comment_index(request):
  """Lists all blog comment."""
    
  if request.method == 'POST':
    comment = Comment.objects.create(title=request.POST.get("title"), reviewer=request.POST.get("reviewer"), email=request.POST.get("email"),content=request.POST.get("content") )
    comment.save()
    form = CommentsForm(request.POST, instance=comment)
    #comments = Comments.objects.all()
  else:
    form = CommentsForm(instance=None)
  comments = Comment.objects.all()
  #pdb.set_trace()
  return SerializeOrRender('blog/comment_index.html', { 'comments': comments }, extra={ 'form': form })

def comments_list(request):
    """Lists all blog comment."""
    
    comments = Comment.objects.all()
    return SerializeOrRender('blog/comments_list.html', { 'comments': comments })

    
def comment_delete(request, comment_id):
    """Deletes the blog post."""
    
    comment = get_object_or_404(Comment.objects.all(), pk=comment_id)
    
    if request.method == 'POST':

        comment.delete()
        return SerializeOrRedirect(reverse('comments_list'), {}, status=CR_DELETED)
    
    else:
        
        return SerializeOrRender('blog/comment_delete.html', { 'comment': comment }, status=CR_CONFIRM)

def comment(request, comment_id=None):
    """Displays, creates or updates a blog comments."""
    
    comment = None
    if comment_id:
        comment = get_object_or_404(Comment.objects.all(), pk=comment_id)

    if request.method == 'POST':
        
        form = CommentsForm(request.POST, instance=comment)
        if form.is_valid():
            comment = form.save()
            return SerializeOrRedirect(reverse('comments_list'), { 'comment': comment })
            
    else:
        
        form = CommentsForm(instance=comment)
    
    return SerializeOrRender('blog/comment.html', { 'comment': comment }, extra={ 'form': form })

