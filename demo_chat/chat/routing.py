from . import consumers
from django.urls import path

websocket_urlspatterns = [
    path('ws/syn/', consumers.MysynConsumer.as_asgi()),
    path('ws/real/', consumers.RealTimeDataConsumer.as_asgi()),
    path('ws/asreal/', consumers.AsyRealTimeDataConsumer.as_asgi())
]