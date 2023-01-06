from django.db import models

from accounts.models import Customer
from service.models import Package, Service


class PackageOrder(models.Model):
    package = models.ForeignKey(Package, on_delete=models.CASCADE)
    customer = models.OneToOneField(Customer, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True, null=True)
    updated = models.DateTimeField(auto_now=True, null=True)


class CustomOrder(models.Model):
    services = models.ManyToManyField(Service)
    customer = models.OneToOneField(Customer, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True, null=True)
    updated = models.DateTimeField(auto_now=True, null=True)
