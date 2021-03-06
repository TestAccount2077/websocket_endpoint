from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter

import TheDistro.routing
import MAS.routing

application = ProtocolTypeRouter({
    # (http->django views is added by default)
    'websocket': AuthMiddlewareStack(
        URLRouter(
            TheDistro.routing.websocket_urlpatterns +
            MAS.routing.websocket_urlpatterns
        )
    )
})
