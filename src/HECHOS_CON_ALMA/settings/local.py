from .base import *


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'info2022fundacion',
        'USER': 'root',
        'PASSWORD': 'mantecoso',
        'HOST': 'localhost',
        'PORT': '3306',

    }
}

