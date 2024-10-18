import os
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
import apps.orders.routing

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'TheOrder.settings')

application = ProtocolTypeRouter({
    'http': get_asgi_application(),
    'websocket': AuthMiddlewareStack(
        URLRouter(
            apps.orders.routing.websocket_urlpatterns
        )
    ),
})
