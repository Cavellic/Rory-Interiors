# Generated by Django 5.0.2 on 2024-05-01 18:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_rename_testimony_testimonial_review'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='name',
        ),
        migrations.AddField(
            model_name='product',
            name='product_type',
            field=models.CharField(choices=[('Couch', 'Couch'), ('Headboard', 'Headboard'), ('Chair', 'Chair'), ('Ottoman', 'Ottoman'), ('Blanket box', 'Blanket box'), ('Lamp shade', 'Lamp shade'), ('Curtain', 'Curtain'), ('Cushion', 'Cushion'), ('Scatter cushion', 'Scatter cushion'), ('Roman blind', 'Roman blind')], max_length=200, null=True),
        ),
    ]
