# Generated by Django 3.2 on 2021-04-26 22:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('temperatures', '0002_rename_temps_temp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='temp',
            name='time_taken',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
