from django.shortcuts import render
from rest_framework.generics import ListAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView, RetrieveAPIView
from ecom.models import Category, Product
from .serializers import CategoryByIdSerializer , ListCategorySerializer , CreateCategorySerializer , UpdateCategorySerializer
from rest_framework.permissions import IsAdminUser

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
    
    