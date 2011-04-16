from piston.handler import BaseHandler, AnonymousBaseHandler
from piston.utils import rc, require_mime, require_extended

from blogserver.apps.blog.models import Post

import pdb

class PostHandler(BaseHandler):
	allowed_methods = ('GET',)

	model = Post
	#anonymous = 'AnonymousPostHandler'
	fields = ('title', 'content', 'created_on', )

	def read(self, request, title=None):
		base = Post.objects
		if title:
			return base.get(title=title)
		else:
			return base.all()

class AddPostHandler(BaseHandler):
	allowed_methods = ('POST', )

	def create(self, request):
		#pdb.set_trace()
		post=Post()
		post.title = request.POST.get("title");
		post.content = request.POST.get("content");
#		post = Post(title, content, author=request.user)
		post.save()
		return post

		"""
		attrs = self.flatten_dict(request.POST)
			
		if self.exists(**attrs):
			return rc.DUPLICATE_ENTRY
		else:
			post = Post(title=attrs['title'], content=attrs['content'], author=request.user)
			post.save()

			return post
		"""

"""
class AnonymousPostHandler(PostHandler, AnonymousBaseHandler):
  # Anonymous entrypoint for blogposts.
  
  fields = ('id', 'title', 'content', 'created_on')
"""
