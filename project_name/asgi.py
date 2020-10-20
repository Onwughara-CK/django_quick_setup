"""
ASGI config for project_name project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

settings = 'project_name.settings.development' if os.environ.get('ENV_ROLE') \
            == 'development' else 'project_name.settings.production'
os.environ.setdefault('DJANGO_SETTINGS_MODULE', settings)

application = get_asgi_application()
