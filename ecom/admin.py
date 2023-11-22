from django.contrib import admin
from ecom.models import Category, Product, Cart , CartItem ,Orders

# Register your models here.

# admin.site.register(Category)
# admin.site.register(Product)
# admin.site.register(Card)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id' , 'name']
    
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id' , 'title' , 'description' ,'created' , 'stock' ,'get_categories']
    
    def get_categories(self , obj):
        return '\n'.join([cat.name for cat in obj.category.all()])
    

@admin.register(CartItem)
class CartItemAdmin(admin.ModelAdmin):
    list_display = ['id' , 'product' ,'quantity']
    
@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    
    list_display = ['id', 'created', 'items']
    
    def items(self , obj):
        return "\n - ".join([cart.product.title for cart in obj.carts.all()])

@admin.register(Orders)
class OrdersAdmin(admin.ModelAdmin):
    
    list_display = ['id' , 'created' , 'items']