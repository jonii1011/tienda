# Generated by Django 5.1.3 on 2024-11-12 04:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tienda', '0002_producto_imagen'),
    ]

    operations = [
        migrations.AlterField(
            model_name='modelo',
            name='version',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]
