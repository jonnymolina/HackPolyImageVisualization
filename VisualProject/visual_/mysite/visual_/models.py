from __future__ import unicode_literals
from django.db import models

class Tag(models.Model):
    tag = models.CharField(max_length=50)

    class Meta:
        ordering = ('tag',)

class Image(models.Model):
    name = models.CharField(max_length=100)
    url = models.TextField(max_length=500)
    tags = models.ForeignKey(Tag, on_delete=models.CASCADE)

    class Meta:
        ordering = ('name',)