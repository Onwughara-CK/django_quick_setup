import dj_database_url
import django_heroku

from project_name.settings.base import *

SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY')

DEBUG = False

ALLOWED_HOSTS = ['.herokuapp.com']

STATICFILES_DIRS = [
    BASE_DIR / 'static',
]

STATIC_ROOT = BASE_DIR / 'staticfiles'

db_from_env = dj_database_url.config(conn_max_age=500)

DATABASES['default'].update(db_from_env)

django_heroku.settings(locals())
