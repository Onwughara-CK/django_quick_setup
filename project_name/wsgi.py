"""
WSGI config for project_name project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application
from django.conf import settings

settings = 'project_name.settings.development' if os.environ.get('ENV_ROLE') == 'development' \
            else 'project_name.settings.production'
os.environ.setdefault('DJANGO_SETTINGS_MODULE', settings)
application = get_wsgi_application()
