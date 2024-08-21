# Generated by Django 5.0.2 on 2024-05-05 21:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_service'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='service',
            name='products',
        ),
        migrations.AddField(
            model_name='service',
            name='products',
            field=models.ManyToManyField(to='main.product'),
        ),
    ]
