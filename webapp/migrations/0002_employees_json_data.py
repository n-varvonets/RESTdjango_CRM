# Generated by Django 3.2.5 on 2021-07-28 06:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='employees',
            name='json_data',
            field=models.JSONField(default='{}'),
        ),
    ]
