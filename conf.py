#-*- coding=utf-8 -*-
#################
#NOT virtualenv # 
#################
import os, sys
import pdb
import django.core.handlers.wsgi
#Calculate the path based on the location of the WSGI script.
apache_configuration= os.path.dirname(__file__)

project = os.path.dirname(apache_configuration)

workspace = os.path.dirname(project)
sys.path.append(workspace)
sys.path.append('/home/jhjguxin/Desktop/djcode',)
sys.path.append('/home/jhjguxin/Desktop/djcode/blogserver',)

os.environ['DJANGO_SETTINGS_MODULE'] = 'blogserver.settings'

os.environ['PYTHON_EGG_CACHE'] = '/tmp'
#上一句能解决Exception occurred processing WSGI script的问题



application = django.core.handlers.wsgi.WSGIHandler()
print >> sys.stderr, sys.path
