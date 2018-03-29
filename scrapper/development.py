from scrapper.settings import *


STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'

DATABASES['default'] = {
    'ENGINE': 'django.db.backends.postgresql',
    'HOST': 'localhost',
    'NAME': 'scrapper',
    'USER': 'hotohete',
    'PASSWORD': 'testtest',
}
