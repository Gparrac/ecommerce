
from rest_framework import viewsets
from apps.products.api.serializers.general_serializer import MeasureUnitSerializer, IndicadorSerializer, CategoryProductSerializer
from apps.base.api import GeneralListApiView
class MeasureUnitViewSet(viewsets.ModelViewSet):
    """ this is a message to left in swagger about this group of routes"""
    serializer_class = MeasureUnitSerializer
    queryset = serializer_class.Meta.model.objects.filter(state = True)
    
class IndicatorViewSet(viewsets.ModelViewSet):
    serializer_class = IndicadorSerializer
    queryset = serializer_class.Meta.model.objects.filter(state = True)

class CategoryProductViewSet(viewsets.ModelViewSet):
    serializer_class = CategoryProductSerializer
    queryset = serializer_class.Meta.model.objects.filter(state = True)
"""
class MeasureUnitListAPIView(GeneralListApiView):
    serializer_class = MeasureUnitSerializer
    
class IndicatorListAPIView(GeneralListApiView):
    serializer_class = IndicadorSerializer

class CategoryProductListAPIView(GeneralListApiView):
    serializer_class = CategoryProductSerializer
"""