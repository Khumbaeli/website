from django.db import models
from ordered_model.models import OrderedModel



class Locations(OrderedModel):
    name = models.CharField(max_length=200)
    latitude = models.FloatField()
    longitude = models.FloatField()
    
        
    def __str__(self):
        return self.name
