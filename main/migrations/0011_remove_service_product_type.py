# Generated by Django 5.0.2 on 2024-05-05 21:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_remove_service_product_type_service_product_type'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='service',
            name='product_type',
        ),
    ]
