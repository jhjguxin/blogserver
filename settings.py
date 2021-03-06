#!/usr/bin/env python
# -*- coding:UTF-8 -*-
# Django settings for mod project.

import os, sys

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
      ('wwew', '905455194@qq.com'),
      ('孤心', '864248765@qq.com'),
    # ('Your Name', 'your_email@domain.com'),
)

MANAGERS = ADMINS

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Fix up piston imports here. We would normally place piston in 
# a directory accessible via the Django app, but this is an
# example and we ship it a couple of directories up.
sys.path.insert(0, os.path.join(BASE_DIR, '../../'))

DATABASE_ENGINE = 'sqlite3'           # 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
DATABASE_NAME = os.path.join(BASE_DIR, 'db')             # Or path to database file if using sqlite3.
#DATABASE_USER = ''             # Not used with sqlite3.
#DATABASE_PASSWORD = ''         # Not used with sqlite3.
#DATABASE_HOST = ''             # Set to empty string for localhost. Not used with sqlite3.
#DATABASE_PORT = ''             # Set to empty string for default. Not used with sqlite3.

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'Asia/Chongqing'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'zh_CN'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# Absolute path to the directory that holds media.
# Example: "/home/media/media.lawrence.com/"
MEDIA_ROOT = os.path.join(BASE_DIR, 'static')

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash if there is a path component (optional in other cases).
# Examples: "http://media.lawrence.com", "http://example.com/media/"
MEDIA_URL = '/static'

# URL prefix for admin media -- CSS, JavaScript and images. Make sure to use a
# trailing slash.
# Examples: "http://foo.com/media/", "/media/".
ADMIN_MEDIA_PREFIX = '/media/'

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'f@vhy8vuq7w70v=cnynm(am1__*zt##i2--i2p-021@-qgws%g'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.load_template_source',
    'django.template.loaders.app_directories.load_template_source',
#     'django.template.loaders.eggs.load_template_source',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    "django.middleware.csrf.CsrfMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.middleware.csrf.CsrfResponseMiddleware",
#    "blogserver.middleware.threadlocals.ThreadLocals",
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'blogserver.pagination.middleware.PaginationMiddleware',
    'dynamicresponse.middleware.api.APIMiddleware',
    'dynamicresponse.middleware.dynamicformat.DynamicFormatMiddleware',
#how to install django-dynamicresponse
#sudo apt-get install python-pip
#pip install django-dynamicresponse

)
TEMPLATE_CONTEXT_PROCESSORS = (
        "django.core.context_processors.auth",
        "django.core.context_processors.debug",
        "django.core.context_processors.i18n",
        "django.core.context_processors.media",
        "django.core.context_processors.request")
ROOT_URLCONF = 'blogserver.urls'

TEMPLATE_DIRS = (
    os.path.join(BASE_DIR, 'templates'),
    os.path.join(BASE_DIR, '../../piston/templates'),
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.sitemaps',
    'django.contrib.admin',
    'django.contrib.admindocs',
    'django.contrib.webdesign',
    'django.contrib.comments',
    'django.contrib.flatpages',
    'django.contrib.markup',
    'blogserver.apps.blog',#我是在根目录创建好app在放在apps下面的如果提示找不到apps.blog则是因为apps目录下面没有__init__.py文件
    'blogserver.apps.about',
    'blogserver.apps.git',
    'blogserver.apps.workblog',
#    'blogserver.api',
#    'blogserver.google_analytics',已经固化在base/html里面了  也可以在 base.html中导入analytics标签即可
    'blogserver.gravatar',
    'blogserver.template_utils',
    'blogserver.pagination',
    'taggit',
    'autoslug',
)
AUTH_PROFILE_MODULE	 = 'profiles.profile'
#FIXTURE_DIRS = (
#    os.path.join(BASE_DIR, 'fixtures'),
#)
ANALYTICS_ID = "UA-25901353-1"
#APPEND_SLASH = False#如果喂False 则不会判断dir后面是否有'/'
