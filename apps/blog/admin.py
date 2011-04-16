#!/usr/bin/env python
# -*- coding:UTF-8 -*-
#admin.py

from django.contrib import admin
from blogserver.apps.blog.models import Comment,User,Post

class PostAdmin(admin.ModelAdmin):
  list_display=('id','title','author','tag','category','created_on','content','hoter',)
#  list_filter=('hoter',)
  search_fields=('title','author','tag','category',)
#  fields=('num','name','img','writer','wdate','notes',)
class CommentAdmin(admin.ModelAdmin):
  list_display=('title','reviewer','email','content','created_on')
#  list_filter=('hoter',)
  search_fields=('title',)
class UserAdmin(admin.ModelAdmin):
  list_display=('id','username','first_name','last_name','name','gender','interest','signature','phone',)
#  list_filter=('hoter',)
  search_fields=('username','first_name','last_name','email',)

admin.site.register(Comment,CommentAdmin)
#admin.site.register(User,UserAdmin)
admin.site.register(Post,PostAdmin)
#admin.site.register(Shop,ShopAdmin)
#admin.site.register(New,NewAdmin)
#admin.site.register(Message,MessageAdmin)
