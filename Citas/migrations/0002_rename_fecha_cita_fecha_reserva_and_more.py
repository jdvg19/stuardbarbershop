# Generated by Django 5.1.2 on 2024-10-20 03:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Citas', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cita',
            old_name='fecha',
            new_name='fecha_reserva',
        ),
        migrations.AddField(
            model_name='cita',
            name='fecha_vencimiento',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
