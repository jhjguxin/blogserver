#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#sitemap.py
from django.contrib.sitemaps import Sitemap
from blogserver.apps.blog.models import Post

class PostSitemap(Sitemap):
  changefreq = "never"
  priority = 0.5


  def items(self):
    return Post.objects.filter(is_draft=False)

  def lastmod(self, obj):
    return obj.date_published
