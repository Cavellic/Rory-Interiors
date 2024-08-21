# Generated by Django 5.0.2 on 2024-05-12 20:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0017_rename_subscribers_subscriber'),
    ]

    operations = [
        migrations.CreateModel(
            name='EmailInteractions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True)),
                ('phone', models.CharField(max_length=20, null=True)),
                ('subject', models.CharField(max_length=200, null=True)),
                ('email', models.EmailField(max_length=100, null=True)),
                ('message', models.TextField(null=True)),
            ],
        ),
    ]
