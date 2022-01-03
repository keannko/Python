from django.db import models
from django.db.models.base import Model

class Phones(models.Model):
    model = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    price = models.CharField(max_length=255)
    photo = models.ImageField(upload_to="photos/%Y/%m/%d")
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)
    cat = models.ForeignKey('Category', on_delete=models.PROTECT)

    def __str__(self):
        return self.title



class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True)

    def __str__(self):
        return self.name

