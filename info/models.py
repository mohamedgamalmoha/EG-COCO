from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class MainInfo(models.Model):
    facebook = models.URLField('Facebook link')
    instagram = models.URLField('Instagram link')
    twitter = models.URLField('Twitter link')
    telegram = models.URLField('Telegram link', blank=True, null=True)
    email = models.EmailField('Web email')
    whatsapp = PhoneNumberField()
    why_us = models.TextField("Why do you choose us?", null=True)
    created = models.DateTimeField(auto_now_add=True, null=True)
    updated = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        verbose_name = 'Website Main Info'
        verbose_name_plural = 'Website Main Info'

    def __str__(self):
        return self.email

    @property
    def whatsapp_link(self):
        return f"https://wa.me/{self.whatsapp}"


class ContactUs(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField(null=True)
    phone_number = PhoneNumberField()
    note = models.TextField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True, null=True)
    updated = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        verbose_name = 'Contact Us'
        verbose_name_plural = 'Contact Us'


class TeamMember(models.Model):
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='members/')
    is_active = models.BooleanField(default=True, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True, null=True)
    updated = models.DateTimeField(auto_now=True, null=True)