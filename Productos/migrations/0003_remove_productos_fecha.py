# Generated by Django 5.1.2 on 2024-10-20 03:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Productos', '0002_productos_delete_estilos'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productos',
            name='fecha',
        ),
    ]
