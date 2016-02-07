from django.db import models
from django.core.validators import URLValidator

# Create your models here.
class Photo(models.Model):
    name = models.CharField(max_length=100)
    url = models.TextField(validators=[URLValidator()])
    # tags = models.ArrayField(
    #     models.CharField(max_length=50, blank=True),
    #     size=none)
    tag1 = models.CharField(max_length=50, blank=True)
    tag2 = models.CharField(max_length=50, blank=True)
    tag3 = models.CharField(max_length=50, blank=True)
    tag4 = models.CharField(max_length=50, blank=True)
    tag5 = models.CharField(max_length=50, blank=True)
    tag6 = models.CharField(max_length=50, blank=True)

class Node(models.Model):
    photo = Photo
    parent = None # this will be a Node
    child1 = None
    child2 = None
    child3 = None
    child4 = None
    child5 = None
    child6 = None