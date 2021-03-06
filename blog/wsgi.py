#!/usr/bin/python3

"""
WSGI config for blog project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/howto/deployment/wsgi/
"""

import os, sys, site
site.addsitedir('/home/samue/blog/blog/lib/python3.4/site-packages')
sys.path.insert(0,'/home/samue/blog/blog')
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "blog.settings")

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

