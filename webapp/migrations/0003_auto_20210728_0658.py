# Generated by Django 3.2.5 on 2021-07-28 06:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0002_employees_json_data'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employees',
            name='emp_id',
        ),
        migrations.RemoveField(
            model_name='employees',
            name='firstname',
        ),
        migrations.RemoveField(
            model_name='employees',
            name='lastname',
        ),
    ]
