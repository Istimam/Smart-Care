# Generated by Django 5.0.6 on 2024-07-12 23:04

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appointment', '0001_initial'),
        ('doctor', '0003_review'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='time',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='doctor.availabletime'),
        ),
    ]
