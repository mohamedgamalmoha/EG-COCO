from rest_framework import serializers

from service.models import Service, Package


class ServiceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Service
        exclude = ('created', 'updated')


class PackageSerializer(serializers.ModelSerializer):

    class Meta:
        model = Package
        exclude = ('created', 'updated')
