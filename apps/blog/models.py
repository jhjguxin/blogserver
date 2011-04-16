#!/usr/bin/env python
# -*- coding:UTF-8 -*-
from django.db import models
from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType
from django.utils.encoding import smart_str
from django.utils.hashcompat import md5_constructor, sha_constructor
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.admin import UserAdmin

class ProfileBase(type):  
  def __new__(cls, name, bases, attrs):  
    module = attrs.pop('__module__')  
    parents = [b for b in bases if isinstance(b, ProfileBase)]  
    if parents:  
      fields = []  
      for obj_name, obj in attrs.items():  
        if isinstance(obj, models.Field): fields.append(obj_name)  
        User.add_to_class(obj_name, obj)  
      UserAdmin.fieldsets = list(UserAdmin.fieldsets)  
      UserAdmin.fieldsets.append((name, {'fields': fields}))  
    return super(ProfileBase, cls).__new__(cls, name, bases, attrs)  
          
class Profile(object):  
  __metaclass__ = ProfileBase  
#用户User
#用户名username first_name*last_name 姓名name 性别gender 密码Password  E-mail：e-mail //(User表单里面有的) 兴趣interest 签名signature 毕业学校university 公司名称f_name 地址address 邮编f_zip 联系电话call 手机phone
GENDER_CHOICES = (
    ('M', 'Male'),
    ('F', 'Female'),
)
class MyProfile(Profile):  
  "the class of B_user"
  name=models.CharField(max_length=30,blank=True)
  gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
  interest=models.CharField(max_length=30,blank=True)
  signature=models.TextField(blank=False)
  birthday = models.DateTimeField(null = True, blank = True)  
  university = models.CharField(max_length = 255, blank = True)  
  f_name=models.CharField(max_length=30)
  address=models.CharField(max_length=30)
  f_zip=models.CharField(max_length=30,blank=True)
  call=models.CharField(max_length=30,blank=True)
  phone=models.CharField(max_length=30,blank=True)


      

  def serialize_fields(self):
    """Only these fields will be included in API responses."""
    return [
            'id',
            'username',
            'password',
            'first_name',
            'last_name',
            'name',
            'gender',
            'interest',
            'signature',
            'birthday',
            'university',
            'email',
            'f_name',
            'address',
            'f_zip',
            'call',
            'phone']

  def is_today_birthday(self):  
    return self.birthday.date() == datetime.date.today()  
      


#评论Comments
#标题title 评论者Reviewer E-mail：e-mail(不显示) 内容content 评论时间created_on
class Comment(models.Model):
  "the class of comments"
  title=models.CharField(max_length=30,blank=False)
  reviewer=models.CharField(max_length=30,blank=False)
  email=models.EmailField(blank=True,verbose_name='e-mail')
  content=models.TextField(blank=False)
  created_on = models.DateTimeField(auto_now_add=True)
  def serialize_fields(self):
    """Only these fields will be included in API responses."""
   
    return [
           'id',
            'title',
            'reviewer',
            'email',
            'content',
            'created_on']

#admin.site.register(Blogpost)

#文章Post
#标题title 作者Author（外键user） 标签tag 分类：category（设定若干固定文章类型） 图片：Image  发布时间created_on 内容content 评论comments（外键） 热度hoter
CATEGORY = (
    (u'日记', u'日记'),
    (u'情感', u'情感'),
    (u'网文', u'网文'),
    (u'专业', u'专业'),
    (u'杂文', u'杂文'),
)
class Tag(models.Model):
  "the class of Tag"
  name = models.CharField(max_length=20,default='tag')

class Post(models.Model):
  "the class of Post"
  title = models.CharField(max_length=255)
  author = models.ForeignKey(User)
  tag=models.ForeignKey(Tag,blank=True,null=True)
  category= models.CharField(max_length=2, choices=CATEGORY)
  img=models.ImageField('Image',upload_to='upload-img')
  created_on = models.DateTimeField(auto_now_add=True)
  content = models.TextField(blank=False)
  comments = models.ForeignKey(Comment,blank=True,null=True)
  hoter=models.IntegerField(blank=True,default=0)
    
  def __unicode__(self):
    return self.title
  def serialize_fields(self):
    """Only these fields will be included in API responses."""
    return [
           'id',
            'title',
            'author',
            'tag',
            'category',
            'img',
            'created_on',
            'content',
            'comments',
            'hoter']


