"""
ASGI config for demo_chat project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/asgi/
"""

import os

from channels.routing import ProtocolTypeRouter, URLRouter
from django.core.asgi import get_asgi_application
from chat.routing import websocket_urlspatterns
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'demo_chat.settings')


application = ProtocolTypeRouter({
    'http' : get_asgi_application(),
    'websocket' : URLRouter(
        websocket_urlspatterns
    )
})
