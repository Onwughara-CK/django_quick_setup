"""
WSGI config for project_name project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

settings = 'project_name.settings.base' if os.environ.get('DJANGO_DEBUG', '') \
         != 'False' else 'project_name.settings.production'
os.environ.setdefault('DJANGO_SETTINGS_MODULE', settings)
application = get_wsgi_application()
