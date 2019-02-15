# Generated by Django 2.1.5 on 2019-02-06 04:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('air_quality', '0002_auto_20190109_0818'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sensor',
            name='unit',
            field=models.CharField(choices=[('mg/m3', 'mg/m3'), ('ppm', 'ppm'), ('g/m3', 'g/m3'), ('PM10', 'PM10'), ('PM2.5', 'PM2.5'), ('μg/m3', 'μg/m3')], help_text='Measurement unit, e.g., mg/m3, ppm, etc.', max_length=256),
        ),
    ]