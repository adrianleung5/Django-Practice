from django.db import models

# Create your models here.
class item (models.model):
    name = models.CharField(max_length=50, null=False)
    done = models.NullBooleanField(null=FALSE, blank=FALSE, default=False)
    
