"""
ASGI config for basic_channel project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/asgi/
"""

import os
from django.core.asgi import get_asgi_application
import first_app.routing

from channels.routing import ProtocolTypeRouter, URLRouter

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'basic_channel.settings')

application = ProtocolTypeRouter({
    'http' : get_asgi_application(),
    'websocket' : URLRouter(
        first_app.routing.websocket_urlpatterns
    )
})