from django.shortcuts import render
from rest_framework.generics import ListAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView, RetrieveAPIView
from ecom.models import Category, Product , Cart
from .serializers import ListProductSerializer, UpdateProductSerializer , CreateProductSerializer, CategoryByIdSerializer , ListCategorySerializer , CreateCategorySerializer , UpdateCategorySerializer
from rest_framework.permissions import IsAdminUser
from rest_framework.views import Response
from .serializers import ListOfProductSerializer

# Create your views here.

class list_category(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = ListCategorySerializer
    
class create_category(CreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CreateCategorySerializer

class get_category(RetrieveAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryByIdSerializer
    
class update_category(UpdateAPIView):
    queryset = Category.objects.all()
    serializer_class = UpdateCategorySerializer
    
class delete_category(DestroyAPIView):
    queryset = Category.objects.all()
    permission_classes = [IsAdminUser]
    
    
# Product Api viezw

class list_products(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ListProductSerializer

class create_product(CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = CreateProductSerializer

class get_product(RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ListProductSerializer
    
class update_product(UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = UpdateProductSerializer
    
class delete_product(DestroyAPIView):
    queryset = Product.objects.all()
    # serializer_class = 
    

# Get product associate to category
class product_of_category(RetrieveAPIView):
    queryset = Product.objects.all()
    
    def get(self, request, pk , *args, **kwargs):
        
        try:
            category_obj = Category.objects.get(id = pk)
        except Category.DoesNotExist:
            return Response({'message':'Category not found'}, status=404)
        
        products_concerns = category_obj.product_set.all()
        
        products_concerns_serializer = ListOfProductSerializer(products_concerns , many=True)
        
        return Response({
            'id':category_obj.id,
            'name':category_obj.name,
            'description':category_obj.description,
            'products':products_concerns_serializer.data
        })
        
    
# Cards Api View
class get_cards(ListAPIView):
    queryset = Cart
    # serializer_class = ListCardSerializer
    pass