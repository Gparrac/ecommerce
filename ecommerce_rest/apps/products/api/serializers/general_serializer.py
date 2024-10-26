from apps.products.models import MeasureUnit, CategoryProduct, Indicator
from rest_framework import serializers


class MeasureUnitSerializer(serializers.ModelSerializer):
    class Meta:
        model = MeasureUnit
        #exclude state due to it's no necessary for users
        exclude = ('state', 'created_date', 'delete_date', 'modified_date')
        
class CategoryProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryProduct
        exclude = ('state', 'created_date', 'delete_date', 'modified_date')

class IndicadorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Indicator
        exclude = ('state', 'created_date', 'delete_date', 'modified_date')