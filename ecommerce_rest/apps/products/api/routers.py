from rest_framework.routers import DefaultRouter
from apps.products.api.views.product_views import ProductViewSet

router = DefaultRouter()

router.register(r'product', ProductViewSet)

urlpatterns = router.urls