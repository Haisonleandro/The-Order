from django.urls import path
from apps.orders.consumers import PedidoConsumer

websocket_urlpatterns = [
    path('ws/pedidos/', PedidoConsumer.as_asgi()),
]
