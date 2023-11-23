from django.db import models
from django_extensions.db.models import TitleDescriptionModel ,  TimeStampedModel , ActivatorModel
from utils.models import Model as modelsId
# Create your models here.

# Model Category
class Category(models.Model):
    
    name = models.CharField(verbose_name='Name' , max_length=200 , blank=False, null=False)
    description = models.CharField(max_length=350 , blank=True)
    
    
    def __str__(self) -> str:
        return f'{self.name}'
    
    class Meta:
        ordering = ['-id']


class Product(TitleDescriptionModel , ActivatorModel, TimeStampedModel):
    
    category = models.ManyToManyField(Category)
    price = models.DecimalField(decimal_places=2 , blank=False, max_digits=12)
    stock = models.IntegerField(default=1)
    
    def __str__(self) -> str:
        return f'{self.title}'
    
    class Meta:
        ordering = ['-id']
        

class CartItem(models.Model):
    
    product = models.ForeignKey(Product , on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    
    def __str__(self) -> str:
        return f'{self.product.title} ({self.quantity})'

class Cart(TimeStampedModel, ActivatorModel , modelsId):
    
    carts = models.ManyToManyField(CartItem , blank=True , null=True)
    
    def __str__(self) -> str:
        names = ','.join([f'{cart.product.title} ({cart.quantity})' for cart in self.carts.all()])
        return f'{names}'
    
    class Meta:
        ordering = ['-created']
        

class Orders(TimeStampedModel, ActivatorModel, modelsId):
    
    options = (
        ('loading' , 'Loading'),
        ('published', 'Published')
    )
    
    items = models.ForeignKey(Cart , on_delete=models.CASCADE)
    status = models.CharField(max_length=30,choices=options , default='loading')
    
    def __str__(self) -> str:
        return f'{self.items}'
    
    # class Meta:
    #     verbose_
