# Generated by Django 3.0 on 2023-03-29 09:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0002_auto_20230329_1459'),
    ]

    operations = [
        migrations.AlterField(
            model_name='staff',
            name='mobile',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='staff',
            name='title',
            field=models.CharField(choices=[('ดช.', 'ดช.'), ('ดญ.', 'ดญ.'), ('นาย', 'นาย'), ('นส.', 'นส.')], max_length=6, null=True),
        ),
    ]
