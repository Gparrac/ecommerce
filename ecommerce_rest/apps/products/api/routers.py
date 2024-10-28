from rest_framework.routers import DefaultRouter
from apps.products.api.views.product_views import ProductViewSet
from apps.products.api.views.general_views import IndicatorViewSet, CategoryProductViewSet, MeasureUnitViewSet
router = DefaultRouter()

router.register(r'products', ProductViewSet, basename='products')
router.register(r'categories-product', CategoryProductViewSet, basename='categories_product'),
router.register(r'measures-unit', MeasureUnitViewSet, basename='measures_units'),
router.register(r'indicators', IndicatorViewSet, basename='indicators')


urlpatterns = router.urls