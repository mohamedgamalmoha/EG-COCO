# Generated by Django 4.1.3 on 2023-01-06 22:05

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ContactUs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254, null=True)),
                ('phone_number', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None)),
                ('note', models.TextField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Contact Us',
                'verbose_name_plural': 'Contact Us',
            },
        ),
        migrations.CreateModel(
            name='MainInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('facebook', models.URLField(verbose_name='Facebook link')),
                ('instagram', models.URLField(verbose_name='Instagram link')),
                ('twitter', models.URLField(verbose_name='Twitter link')),
                ('telegram', models.URLField(blank=True, null=True, verbose_name='Telegram link')),
                ('email', models.EmailField(max_length=254, verbose_name='Web email')),
                ('whatsapp', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None)),
                ('why_us', models.TextField(null=True, verbose_name='Why do you choose us?')),
            ],
            options={
                'verbose_name': 'Website Main Info',
                'verbose_name_plural': 'Website Main Info',
            },
        ),
        migrations.CreateModel(
            name='TeamMember',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('title', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='members/')),
            ],
        ),
    ]
