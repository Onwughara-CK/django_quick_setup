from project_name.settings.base import *


ALLOWED_HOSTS = ['.herokuapp.com']




import dj_database_url
import django_heroku
db_from_env = dj_database_url.config(conn_max_age=500)
DATABASES['default'].update(db_from_env)
django_heroku.settings(locals())
