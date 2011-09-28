tag = forms.CharField(label=_("tag"), max_length=30, help_text = _("请输入标签并以逗号隔开."),error_messages = {'invalid': _("超出长度限制或者输入有误.")})

"""
def save(self, commit=True):
    user = super(UserCreationForm, self).save(commit=False)
    user.set_password(self.cleaned_data["password1"])
    if commit:
        user.save()
    return post
"""
def save(self,):
    tag = super(PostsForm, self).save(commit=False)
    user.set_password(self.cleaned_data["password1"])
    if commit:
        user.save()
    return post

<QueryDict: {u'status': [u'1'], u'category': [u'3'], u'_save': [u'\u4fdd\u5b58'], u'img': [u''], u'title': [u'12313'], u'content': [u'<p>\u554a\u53d1\u9001\u53d1\u9001</p>'], u'tag': [u'42', u'53', u'30'], u'csrfmiddlewaretoken': [u'd9bf998c378158d24d8fd4b893b5789b', u'd9bf998c378158d24d8fd4b893b5789b'], u'slug': [u'12313']}>


    def save(self,commit=True,*args, **kwargs):
        post = super(PostsForm, self).save()
        #pdb.set_trace()
        #tag_slug=auto_tag_slug()
        try:
            tags=self.data.get(u'tag')
        except:
            raise forms.ValidationError(_("get tag failed please check and try again..."))
        tags_list=tags.split(' ')
        #self.data[u'tag']=[]
        tagsdblist=[]
        pdb.set_trace()
        for tag in tags_list:
            if tag:
                p, created=Tag.objects.get_or_create(name=tag,slug=auto_tag_slug())
                post.tag.add(p)




        if commit:
            post.save()
        return post







model.py


    for tag in self.tags_list:
        if tag:
            p, created=Tag.objects.get_or_create(name=tag,slug=auto_tag_slug())
            post.tag.add(p)
