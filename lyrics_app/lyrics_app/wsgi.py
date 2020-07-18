"""
WSGI config for lyrics_app project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application
# from dotenv import load_dotenv

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'lyrics_app.settings')
os.environ.setdefault('IS_DEV', 'true')

application = get_wsgi_application()


# project_folder = os.path.expanduser('~/lyrics_app')  # adjust as appropriate
# load_dotenv(os.path.join(project_folder, '.env'))
