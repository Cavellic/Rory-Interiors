# Generated by Django 5.0.2 on 2024-05-07 22:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0015_service_product'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subscribers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=200, null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='product',
            name='service_type',
        ),
        migrations.AddField(
            model_name='product',
            name='name',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.DeleteModel(
            name='Service',
        ),
        migrations.DeleteModel(
            name='ServiceType',
        ),
    ]
