#!/usr/bin/env python
# -*- coding: UTF-8 -*-
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.utils.translation import ugettext as _
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.core.urlresolvers import reverse
from django.contrib.auth.forms import PasswordResetForm,PasswordChangeForm,AdminPasswordChangeForm
#from django.contrib.auth.models import User

from dynamicresponse.response import *

from forms import *
from models import *

from django.views.decorators.csrf import csrf_exempt
import pdb

"""
def users(request):
    users = Users.objects.all()

    return render_to_response("users.html", {
        'users': users },
        RequestContext(request))
    
def test_js(request):
    return render_to_response('test_js.html', {}, RequestContext(request))
"""
"""
@ csrf_exempt
def index_user(request):
  "Lists all blog user."
    
  if request.method == 'POST':
    user = User.objects.create(title=request.POST.get("title"), reviewer=request.POST.get("reviewer"), email=request.POST.get("email"),content=request.POST.get("content") )
    user.save()
    form = RegisterForm(request.POST, instance=user)
    #users = Users.objects.all()
  else:
    form = RegisterForm(instance=None)
  users = User.objects.all()
  #pdb.set_trace()
  return SerializeOrRender('blog/index_user.html', { 'users': users }, extra={ 'form': form })
"""
def users_list(request):
    "Lists all blog user."
    
    users = User.objects.all()
    return SerializeOrRender('blog/users_list.html', { 'users': users })

"""    
def delete_user(request, user_id):
    "Deletes the blog user."
    
    user = get_object_or_404(User.objects.all(), pk=user_id)
    
    if request.method == 'POST':

        user.delete()
        return SerializeOrRedirect(reverse('list_users'), {}, status=CR_DELETED)
    
    else:
        
        return SerializeOrRender('blog/delete_user.html', { 'user': user }, status=CR_CONFIRM)
"""
def register(request, user_id=None):
    """Displays, creates or updates a blog users."""
    
    user = None
    if user_id:
        user = get_object_or_404(User.objects.all(), pk=user_id)

    if request.method == 'POST':
        
        form = RegisterForm(request.POST, instance=user)
        if form.is_valid():
            user = form.save()
            return SerializeOrRedirect(reverse('users_list'), { 'user': user })
            
    else:
        
        form = RegisterForm(instance=user)
    
    return SerializeOrRender('blog/user.html', { 'user': user }, extra={ 'form': form })
def u_change(request, user_id=None):
    """Displays, creates or updates a blog users."""
    
    user = None
    if user_id:
        user = get_object_or_404(User.objects.all(), pk=user_id)

    if request.method == 'POST':
        
        form = U_ChangeForm(request.POST, instance=user)
        if form.is_valid():
            user = form.save()
            return SerializeOrRedirect(reverse('users_list'), { 'user': user })
            
    else:
        
        form = U_ChangeForm(instance=user)
    
    return SerializeOrRender('blog/user.html', { 'user': user }, extra={ 'form': form })
def passwordchange(request, user_id=None):
    password_change_form=PasswordChangeForm
    user = None
    if user_id:
        user = get_object_or_404(User.objects.get(id=user_id), pk=user_id)
    if request.method == 'POST':
        form = PasswordChangeForm(user, request.POST)
        if form.is_valid():
            user = form.save()
            return SerializeOrRedirect(reverse('list_users'), { 'user': user })
            
    else:
        
        form = password_change_form(user)
    
    return SerializeOrRender('blog/user.html', { 'user': user }, extra={ 'form': form })
"""
def passwordchange(request, user_id=None):

    "Displays, creates or updates a blog users."
    
    user = None
    if user_id:
        user = get_object_or_404(User.objects.all(), pk=user_id)
    olduser=User.objects.get(id=user_id)
    if request.method == 'POST':
        
        form = U_PasswordChangeForm(request.POST, instance=user)
        if form.is_valid():
            user = form.save()
            return SerializeOrRedirect(reverse('list_users'), { 'user': user })
            
#    else:
#        form = U_PasswordChangeForm(instance=user)
    
    return SerializeOrRender('blog/user.html', { 'user': user }, extra={ 'form': form })
"""
"""
def passwordchange(request, is_admin_site=False, template_name='blog/user.html',
        email_template_name='registration/password_reset_email.html',
        password_reset_form=PasswordResetForm, token_generator=default_token_generator,
        post_reset_redirect=None):
    if post_reset_redirect is None:
        post_reset_redirect = reverse('django.contrib.auth.views.password_reset_done')
    if request.method == "POST":
        form = password_reset_form(request.POST)
        if form.is_valid():
            opts = {}
            opts['use_https'] = request.is_secure()
            opts['token_generator'] = token_generator
            if is_admin_site:
                opts['domain_override'] = request.META['HTTP_HOST']
            else:
                opts['email_template_name'] = email_template_name
                if not Site._meta.installed:
                    opts['domain_override'] = RequestSite(request).domain
            form.save(**opts)
            return HttpResponseRedirect(post_reset_redirect)
    else:
        form = password_reset_form()
    return render_to_response(template_name, {
        'form': form,
    }, context_instance=RequestContext(request))
"""

