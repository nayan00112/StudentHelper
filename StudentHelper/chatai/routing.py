from django.urls import path
from . import consumers

websocket_urlpatterns = [
    path('ws/as/chat_ai/', consumers.MyAsyncChat.as_asgi()),
]