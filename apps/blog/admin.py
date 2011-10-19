#!/usr/bin/env python
# -*- coding:UTF-8 -*-
#admin.py

from django.contrib import admin
from blogserver.apps.blog.models import Comment,User,Post, Category, Tag,Link
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserChangeForm
from django.utils.translation import ugettext, ugettext_lazy as _
import pdb
from blogserver.apps.blog.forms import PostsForm

def tags(obj):
    return ", ".join([x.name for x in obj.tag.all()])

def categories(obj):
    #pdb.set_trace()
    return obj.category.name

def author(obj):
    return obj.author.get_full_name()

def post_count(obj):
    return obj.post_set.count()

class PostAdmin(admin.ModelAdmin):


    prepopulated_fields = {
        'slug': ('title',),
    }
    date_hierarchy = 'created_on'
    list_display = ('title', 'status', author , 'created_on','date_published', 'date_modified', tags, categories)
    list_filter = ('status', 'tag', 'category',"author")
    search_fields = ('title','author__username','category__name','^author__first_name', '^author__last_name',)
    exclude = ('author',)
    actions = ['make_published']

    form=PostsForm

    def queryset(self, request):
        """
        Returns a QuerySet of all model instances that can be edited by the
        admin site. This is used by changelist_view.
        """
        #pdb.set_trace()
        #super(PostAdmin, self)
        #qs = self.model.live
        qs = super(PostAdmin, self).queryset(request).model.objects.all()
        # TODO: this should be handled by some parameter to the ChangeList.
        ordering = super(PostAdmin, self).ordering
        if ordering:
            qs = qs.order_by(*ordering)
        return qs

    def make_published(self, request, queryset):
        rows_updated = queryset.update(status=1)
        if rows_updated == 1:
            message_bit = "1 story was"
        else:
            message_bit = "%s stories were" % rows_updated
        self.message_user(request, "%s successfully marked as published." % message_bit)
    def save_model(self, request, obj, *args, **kargs):
        obj.author = request.user;
        super(PostAdmin, self).save_model(request, obj, *args, **kargs)    

    
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {
        'slug': ('name',),
    }

class TagAdmin(admin.ModelAdmin):
    list_display = ('name', post_count)

    prepopulated_fields = {
        'slug': ('name',),
    }
class LinkAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_on'
    list_display = ('name', 'url', 'describe' , 'created_on','date_modified',)
    list_filter = ('name', 'url', 'created_on')
    search_fields = ('name','url',)

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
admin.site.register(Link, LinkAdmin)
#admin.site.register(Shop,ShopAdmin)
#admin.site.register(New,NewAdmin)
#admin.site.register(Message,MessageAdmin)
