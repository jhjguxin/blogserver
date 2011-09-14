#!/usr/bin/env python
# -*- coding:UTF-8 -*-
#admin.py

from django.contrib import admin
from blogserver.apps.blog.models import Comment,User,Post, Category, Tag
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserChangeForm
from django.utils.translation import ugettext, ugettext_lazy as _


def tags(obj):
    return ", ".join([x.name for x in obj.tag.all()])

def categories(obj):
    return ", ".join([c.name for c in obj.categories.all()])

def author(obj):
    return obj.author.get_full_name()

class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {
        'slug': ('title',),
    }
    date_hierarchy = 'created_on'
    list_display = ('title', 'status', author , 'created_on','date_published', 'date_modified', tags, categories)
    list_filter = ('status', 'tag', 'categories')
    search_fields = ('title','author','tag','categories',)
    exclude = ('author',)
    
    def save_model(self, request, obj, *args, **kargs):
        obj.author = request.user;
        super(PostAdmin, self).save_model(request, obj, *args, **kargs)
    
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {
        'slug': ('name',),
    }

class TagAdmin(admin.ModelAdmin):
    prepopulated_fields = {
        'slug': ('name',),
    }

#class PostAdmin(admin.ModelAdmin):
#    list_display=('id','title','author','tag','category','created_on','content','hoter',)
#  list_filter=('hoter',)
#    search_fields=('title','author','tag','category',)
#  fields=('num','name','img','writer','wdate','notes',)
#class CommentAdmin(admin.ModelAdmin):
#    list_display=('title','reviewer','email','content','created_on')
#  list_filter=('hoter',)
    search_fields=('title',)
class CustomUserChangeForm(UserChangeForm):
    """updates a blog user."""
    class Meta:
        model = User
        fields =('id','username','password','groups','first_name','last_name','name','gender','birthday','interest','university','signature','email','f_name','address','f_zip','call','phone','last_login','date_joined','is_active','is_staff','is_superuser','user_permissions')

class CustomUserAdmin(UserAdmin):
    fieldsets = (
  	        (None, {'fields': ('username', 'password')}),
  	        (_('Personal info'), {'fields': ('first_name','last_name','name','gender','interest','signature','birthday','university','email','f_name','address','f_zip','call','phone')}),
  	        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser', 'user_permissions')}),
  	        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
  	        (_('Groups'), {'fields': ('groups',)}),
      	        )
    form = CustomUserChangeForm

#admin.site.register(Comment,CommentAdmin)
#admin.site.register(User,UserAdmin)
admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin) 
admin.site.register(Post,PostAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Tag, TagAdmin)
#admin.site.register(Shop,ShopAdmin)
#admin.site.register(New,NewAdmin)
#admin.site.register(Message,MessageAdmin)
