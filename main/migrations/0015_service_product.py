# Generated by Django 5.0.2 on 2024-05-05 22:44

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0014_alter_service_service_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='product',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main.product'),
        ),
    ]
