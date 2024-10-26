
from apps.products.api.serializers.general_serializer import MeasureUnitSerializer, IndicadorSerializer, CategoryProductSerializer
from apps.base.api import GeneralListApiView

class MeasureUnitListAPIView(GeneralListApiView):
    serializer_class = MeasureUnitSerializer
    
class IndicatorListAPIView(GeneralListApiView):
    serializer_class = IndicadorSerializer

class CategoryProductListAPIView(GeneralListApiView):
    serializer_class = CategoryProductSerializer