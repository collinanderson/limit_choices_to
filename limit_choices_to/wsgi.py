"""
WSGI config for limit_choices_to project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/dev/howto/deployment/wsgi/
"""

import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "limit_choices_to.settings")

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
