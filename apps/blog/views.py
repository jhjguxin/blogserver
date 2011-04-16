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
def index_comment(request):
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
  return SerializeOrRender('blog/index_comment.html', { 'comments': comments }, extra={ 'form': form })

def list_comments(request):
    """Lists all blog comment."""
    
    comments = Comment.objects.all()
    return SerializeOrRender('blog/list_comments.html', { 'comments': comments })

    
def delete_comment(request, comment_id):
    """Deletes the blog post."""
    
    comment = get_object_or_404(Comment.objects.all(), pk=comment_id)
    
    if request.method == 'POST':

        comment.delete()
        return SerializeOrRedirect(reverse('list_comments'), {}, status=CR_DELETED)
    
    else:
        
        return SerializeOrRender('blog/delete_comment.html', { 'comment': comment }, status=CR_CONFIRM)

def comment(request, comment_id=None):
    """Displays, creates or updates a blog comments."""
    
    comment = None
    if comment_id:
        comment = get_object_or_404(Comment.objects.all(), pk=comment_id)

    if request.method == 'POST':
        
        form = CommentsForm(request.POST, instance=comment)
        if form.is_valid():
            comment = form.save()
            return SerializeOrRedirect(reverse('list_comments'), { 'comment': comment })
            
    else:
        
        form = CommentsForm(instance=comment)
    
    return SerializeOrRender('blog/comment.html', { 'comment': comment }, extra={ 'form': form })

