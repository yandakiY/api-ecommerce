from rest_framework.serializers import ModelSerializer, Serializer
from ecom.models import Category, Product


class ListCategorySerializer(ModelSerializer):
    
    class Meta:
        model = Category
        fields = [
            'id',
            'name',
            'description'
        ]

class UpdateCategorySerializer(ModelSerializer):
    
    class Meta:
        model = Category
        fields = [
            'id',
            'name',
            'description'
        ]
        
class CreateCategorySerializer(ModelSerializer):
    
    class Meta:
        model = Category
        fields = [
            'id',
            'name',
            'description'
        ]

class CategoryByIdSerializer(ModelSerializer):
    
    class Meta:
        model = Category
        fields = [
            'id',
            'name',
            'description'
        ]