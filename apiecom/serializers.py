from rest_framework.serializers import ModelSerializer, Serializer
from ecom.models import Category, Product
from rest_framework import fields


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


class CategorySerializer(ModelSerializer):
    
    class Meta:
        model = Category
        fields = '__all__'

        
class ListProductSerializer(ModelSerializer):
    
    name = fields.CharField(source = 'title' , required= True)
    categories = CategorySerializer(source = 'category',many = True)
    
    class Meta:
        model = Product
        fields = [
            'id',
            'name',
            'description',
            'created',
            'categories',
            'price'
        ]

class CreateProductSerializer(ModelSerializer):
    
    name = fields.CharField(source = 'title' , required=True)
    
    class Meta:
        model = Product
        fields = [
            'name',
            'description',
            'price',
            'category'
        ]
        

class UpdateProductSerializer(ModelSerializer):
    
    name = fields.CharField(source='title', required=True)
    
    class Meta:
        model = Product
        fields = [
            'name',
            'description',
            'category',
            'price'
        ]