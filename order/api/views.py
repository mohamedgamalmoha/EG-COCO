from rest_framework import generics, permissions

from .serializers import PackageOrderSerializer, CustomOrderSerializer


class PackageOrderCreateAPIView(generics.CreateAPIView):
    serializer_class = PackageOrderSerializer
    permission_classes = [permissions.AllowAny]


class CustomOrderCreateAPIView(generics.CreateAPIView):
    serializer_class = CustomOrderSerializer
    permission_classes = [permissions.AllowAny]
