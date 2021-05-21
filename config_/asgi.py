"""
ASGI config for config_ project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/asgi/
"""
#novo no Django a partir da versão 3.0, que permite um opcional Interface Gateway de Servidor Assíncrono a ser executado.
import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config_.settings')

application = get_asgi_application()
