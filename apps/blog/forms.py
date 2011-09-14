from django import forms
from blogserver.apps.blog.models import Post
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,UserChangeForm,PasswordChangeForm
from blogserver.apps.blog.models import Comment,User,Post, Category, Tag
"""
class CommentsForm(forms.ModelForm):
    "Creates/updates a blog post."
    
    class Meta:
        model = Comment
        fields = ('id','title','reviewer','email','content',)
"""
class PostsForm(forms.ModelForm):
    """Creates/updates a blog post."""
    #tag = forms.ModelMultipleChoiceField(queryset=Tag.objects.all())    
    class Meta:
        model = Post
        fields = ('id','title','author','slug','status','tag','categories','img','content',)
#        fields = ('id','title','author','tag','categories','content','hoter',)

class RegisterForm(UserCreationForm):
    """Creates a blog user."""
    
    class Meta:
        model = User
        fields = ('id','username','password1','password2','first_name','last_name','name','gender','interest','signature','email','f_name','address',            'f_zip','call','phone')
class U_ChangeForm(UserChangeForm):
    """updates a blog user."""
    
    class Meta:
        model = User
        fields = ('id','username','name','first_name','last_name','gender','interest','signature','email','f_name','address','f_zip','call','phone')

class U_PasswordChangeForm(PasswordChangeForm):
    """updates a blog user."""
    
    class Meta:
        model = User
        fields = ('id','old_password','password1','password2',)

