"""WSGI config for Comic Reader."""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "comic_reader.settings")

application = get_wsgi_application()
