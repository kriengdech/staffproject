# Generated by Django 3.0 on 2023-04-19 09:26

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0003_auto_20230329_1638'),
    ]

    operations = [
        migrations.AddField(
            model_name='staff',
            name='birthdate',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='staff',
            name='bloodgrp',
            field=models.CharField(choices=[('A', 'A'), ('B', 'B'), ('O', 'O'), ('AB', 'AB')], max_length=5, null=True),
        ),
    ]
