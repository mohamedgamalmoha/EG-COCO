# Generated by Django 4.1.3 on 2023-01-20 18:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0003_company_faqs_previousproject_subscribedemails_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='created',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='company',
            name='updated',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]