"""ASGI config for Comic Reader."""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "comic_reader.settings")

application = get_asgi_application()
