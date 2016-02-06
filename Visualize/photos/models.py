from django.db import models
from django.core.validators import URLValidator

# Create your models here.
class Photo(models.Model):
    name = models.CharField(max_length=100)
    url = models.TextField(validators=[URLValidator()])
    