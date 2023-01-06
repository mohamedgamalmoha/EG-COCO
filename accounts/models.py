from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractUser, UserManager
from phonenumber_field.modelfields import PhoneNumberField


class CustomUserManager(UserManager):

    def create_superuser(self, username, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_active', True)
        return super(CustomUserManager, self).create_superuser(username, email, password, **extra_fields)


class User(AbstractUser):
    email = models.EmailField(_("email address"), unique=True)
    phone_number = PhoneNumberField(unique=True, null=False, blank=False)

    REQUIRED_FIELDS = ['username', ]
    USERNAME_FIELD = 'username'

    objects = CustomUserManager()

    class Meta(AbstractUser.Meta):
        swappable = "AUTH_USER_MODEL"

    def __str__(self):
        return self.email


class Customer(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField(null=True)
    phone_number = PhoneNumberField()
    note = models.TextField(null=True, blank=True)
