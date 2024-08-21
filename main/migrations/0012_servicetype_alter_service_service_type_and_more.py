# Generated by Django 5.0.2 on 2024-05-05 21:48

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_remove_service_product_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='ServiceType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service_types', models.CharField(max_length=30, null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='service',
            name='service_type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main.product'),
        ),
        migrations.AddField(
            model_name='product',
            name='service_type',
            field=models.ManyToManyField(null=True, to='main.servicetype'),
        ),
    ]
