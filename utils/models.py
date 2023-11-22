import uuid
from django.db import models

class Model(models.Model):
    '''
        Generate a id basedon uuid
    '''
    
    id = models.UUIDField(primary_key=True , default=uuid.uuid4)
    
    class Meta:
        abstract = True