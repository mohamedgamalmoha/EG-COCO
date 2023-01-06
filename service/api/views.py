from rest_framework import generics, permissions

from service.models import Service, Package
from .serializers import ServiceSerializer, PackageSerializer


class ServiceListAPIView(generics.ListAPIView):
    queryset = Service.objects.filter(is_active=True)
    serializer_class = ServiceSerializer
    permission_classes = [permissions.AllowAny]


class PackageListAPIView(generics.ListAPIView):
    queryset = Package.objects.filter(is_active=True)
    serializer_class = PackageSerializer
    permission_classes = [permissions.AllowAny]
