from rest_framework.routers import DefaultRouter
from apps.orders.api.views import ProductoViewSet, PedidoViewSet, ClienteViewSet, RestauranteViewSet

router = DefaultRouter()
router.register(r'productos', ProductoViewSet)
router.register(r'pedidos', PedidoViewSet)
router.register(r'clientes', ClienteViewSet)
router.register(r'restaurantes', RestauranteViewSet)

urlpatterns = router.urls
