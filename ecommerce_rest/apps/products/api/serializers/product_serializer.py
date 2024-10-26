from apps.products.models import Product
from rest_framework import serializers
from apps.products.api.serializers.general_serializer import MeasureUnitSerializer, CategoryProductSerializer
class ProductSerializer(serializers.ModelSerializer):
    """ options to relate serializer fields with foreign fields 
    1. firstone appends fields like and a dict with its keys as well
        measure_unit = MeasureUnitSerializer()
        category = CategoryProductSerializer()
    2. second replace the atribute with str's function of foreign model
        measure_unit = serializers.StringRelatedField()
        category = serializers.StringRelatedField()
    3. thid way is use to_representation function to rewrite the 
        serializer's structure  however if we use before options the type foregn props
        won't load like selectors in django html interface when we aim to post endpoint
    """

    class Meta:
        model = Product
        exclude = ('state', 'created_date', 'modified_date', 'delete_date',)
    
    def to_representation(self, instance):
        return {
            'id': instance.id,
            'description': instance.description,
            'image': instance.image or '',
            'measure_unit': instance.measure_unit.description,
            'category': instance.category.description
        }