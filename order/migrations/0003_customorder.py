# Generated by Django 4.1.3 on 2023-01-06 21:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_alter_customer_note'),
        ('service', '0003_package_created_package_updated_service_created_and_more'),
        ('order', '0002_packageorder_created_packageorder_updated'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomOrder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated', models.DateTimeField(auto_now=True, null=True)),
                ('customer', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='accounts.customer')),
                ('services', models.ManyToManyField(to='service.service')),
            ],
        ),
    ]
