from video_service.settings.base import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'aprende24',
        'USER': 'aprende24',
        'HOST': 'db-dev', # set in docker-compose.yml
        'PORT': '5432' # default postgres port
    }
}


DEBUG = True

MEDIA_ROOT = MEDIA_DIR
MEDIA_URL = '/media/'

SECRET_KEY = 'nw12ih71!t88tf#xrk76zsomn)e2xq2zssypnd@#))_!ke!p4b'

ALLOWED_HOSTS = ["*"]
