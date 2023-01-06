from rest_framework import serializers
from djoser.serializers import UserCreateSerializer

from accounts.models import Customer


class UserRegistrationSerializer(UserCreateSerializer):

    class Meta(UserCreateSerializer.Meta):
        fields = ('id', 'email', 'username', 'phone_number', 'password')


class CustomerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Customer
        exclude = ()

