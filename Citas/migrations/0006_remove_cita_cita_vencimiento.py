# Generated by Django 5.1.2 on 2024-10-24 01:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Citas', '0005_alter_cita_reserva_cita'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cita',
            name='cita_vencimiento',
        ),
    ]