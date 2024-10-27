from django.urls import path
from apps.products.api.views.general_views import MeasureUnitListAPIView, CategoryProductListAPIView, IndicatorListAPIView
# from apps.users.api.api import UserApiView
from apps.products.api.views.product_views import  ProductListCreateApiView, ProductRetriveUpdateDestroyApiView, ProductRetrieveAPIView, ProductDestroyAPIView, ProductUpdateAPIview

urlpatterns = [
    path('measure_unit/', MeasureUnitListAPIView.as_view(), name = 'measure_unit'),
    path('indicator/', IndicatorListAPIView.as_view(), name = 'measure_unit'),
    path('category_product/', CategoryProductListAPIView.as_view(), name = 'measure_unit'),    
    # path('product/', ProductListCreateApiView.as_view(), name = 'product_create and list'),
    # path('product/retrieve-update-destroy/<int:pk>', ProductRetriveUpdateDestroyApiView.as_view(), name = 'product_retrieve')

]