#-*- coding=utf-8 -*-
import os, sys
import pdb


#Calculate the path based on the location of the WSGI script.
apache_configuration= os.path.dirname(__file__)

project = os.path.dirname(apache_configuration)

workspace = os.path.dirname(project)
#sys.path.append(workspace)
sys.path.append('/var/www',)

#activate_this = '/var/www/blogserver/bin/activate_this.py'
#execfile(activate_this, dict(__file__=activate_this))

#sys.path.append(workspace + '/blogserver',)
##其實 mod_wsgi 2.0 之後的版本, 可以很方便的來使用 virtualenv, 如果你是 apache + mod_wsgi 的話 XD
#只要在你的 wsgi file 加上這一段即可
import site
site.addsitedir(project+'/blogserver/lib/python2.7/site-packages') 

os.environ['DJANGO_SETTINGS_MODULE'] = 'blogserver.settings'

os.environ['PYTHON_EGG_CACHE'] = '/tmp'
#上一句能解决Exception occurred processing WSGI script的问题


import django.core.handlers.wsgi

application = django.core.handlers.wsgi.WSGIHandler()
print >> sys.stderr, sys.path
