from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Lovinoo.settings")
# Initialize Django ASGI application early to ensure the AppRegistry
# is populated before importing code that may import ORM models.
from django.core.asgi import get_asgi_application
django_asgi_app = get_asgi_application()
from chat import routing as echo_routing

application = ProtocolTypeRouter({
    "http": django_asgi_app,
    'websocket': AuthMiddlewareStack(
        URLRouter(
            echo_routing.websocket_urlpatterns
        )
    )
})