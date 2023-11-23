from rest_framework.serializers import ModelSerializer, Serializer
from ecom.models import Category, Product , Cart , CartItem, Orders
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



# Product Serializer 
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
            'stock',
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
            'stock',
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
            'stock',
            'category',
            'price'
        ]

# get products for category associate

class ListOfProductSerializer(ModelSerializer):
    
    name = fields.CharField(source = 'title' , required= True)
    
    class Meta:
        model = Product
        fields = [
            'id',
            'name',
            'description',
            'stock',
            'created',
            'price'
        ]
class ProductForCategory(ModelSerializer):
    
    id = fields.CharField()
    name = fields.CharField()
    description = fields.CharField()
    stock = fields.IntegerField()
    categories = ListOfProductSerializer(many = True)
    


# # Cart item serializers
# class ProductSerializer(ModelSerializer):
    
#     class Meta:
#         model = Product
#         fields = '__all__'
# class ListCartItemSerializer(ModelSerializer):
    
#     # products = ProductSerializer(source='product' , many = True)
#     class Meta:
#         model = CartItem
#         fields = [
#             'id',
#             'quantity',
#             'product'
#         ]



# class ListCartSerializer(ModelSerializer):
    
#     # carts =
#     class Meta:
#         model = Cart
#         fields = '__all__'

# class CreateCartSerializer(ModelSerializer):
    
#     class Meta:
#         model = Cart
#         fields = [
#             'carts'
#         ]