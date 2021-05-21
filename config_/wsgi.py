"""
WSGI config for config_ project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/wsgi/
"""
#que significa Web Server Interface de gateway, ajuda o Django a servir nossas eventuais páginas da web
import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config_.settings')

application = get_wsgi_application()
