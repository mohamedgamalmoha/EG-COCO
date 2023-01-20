from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class MainInfo(models.Model):
    facebook = models.URLField('Facebook link')
    instagram = models.URLField('Instagram link')
    twitter = models.URLField('Twitter link')
    telegram = models.URLField('Telegram link', blank=True, null=True)
    email = models.EmailField('Web email')
    whatsapp = PhoneNumberField()
    address = models.CharField("Company Address", null=True, max_length=500)
    why_us = models.TextField("Why do you choose us?", null=True)
    about_us = models.TextField("Who are we?", null=True)
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


class FAQs(models.Model):
    quote = models.CharField(max_length=1000)
    answer = models.TextField()
    active = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True, null=True)
    updated = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        verbose_name = 'FAQ'
        verbose_name_plural = 'FAQs'

    def __str__(self):
        return self.quote


class PreviousProject(models.Model):
    name = models.CharField(max_length=1000)
    description = models.TextField()
    image = models.ImageField(upload_to='projects/')
    active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True, null=True)
    updated = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        verbose_name = 'Previous Work'
        verbose_name_plural = 'Previous Works'

    def __str__(self):
        return self.name


class SubscribedEmails(models.Model):
    email = models.EmailField()
    created = models.DateTimeField(auto_now_add=True, null=True)
    updated = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.email


class Company(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='companies/')
    active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True, null=True)
    updated = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.name
