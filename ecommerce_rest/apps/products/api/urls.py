from django.urls import path
from apps.products.api.views.general_views import MeasureUnitListAPIView, CategoryProductListAPIView, IndicatorListAPIView
# from apps.users.api.api import UserApiView
from apps.products.api.views.product_views import  ProductListCreateApiView, ProductRetrieveAPIView, ProductDestroyAPIView, ProductUpdateAPIview

urlpatterns = [
    path('measure_unit/', MeasureUnitListAPIView.as_view(), name = 'measure_unit'),
    path('indicator/', IndicatorListAPIView.as_view(), name = 'measure_unit'),
    path('category_product/', CategoryProductListAPIView.as_view(), name = 'measure_unit'),    
    path('product/', ProductListCreateApiView.as_view(), name = 'product_create and list'),
    path('product/retrieve/<int:pk>', ProductRetrieveAPIView.as_view(), name = 'product_retrieve'),
    path('product/destroy/<int:pk>', ProductDestroyAPIView.as_view(), name = 'product_destroy'),
    path('product/update/<int:pk>', ProductUpdateAPIview.as_view(), name = 'product_update')
]