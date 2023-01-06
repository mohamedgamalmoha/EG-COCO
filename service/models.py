from django.db import models
from ckeditor.fields import RichTextField


class Service(models.Model):
    name = models.CharField(max_length=100)
    icon = models.ImageField(upload_to="service/")
    description = models.TextField()
    is_active = models.BooleanField(default=True, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True, null=True)
    updated = models.DateTimeField(auto_now=True, null=True)


class Package(models.Model):
    name = models.CharField(max_length=100)
    services = models.ManyToManyField(Service)
    description = RichTextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    is_featured = models.BooleanField(default=False, blank=True, null=True)
    is_active = models.BooleanField(default=True, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True, null=True)
    updated = models.DateTimeField(auto_now=True, null=True)
