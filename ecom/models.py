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
        
   
