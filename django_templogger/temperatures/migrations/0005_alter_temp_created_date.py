# Generated by Django 3.2 on 2021-04-28 20:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('temperatures', '0004_rename_time_taken_temp_created_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='temp',
            name='created_date',
            field=models.DateTimeField(),
        ),
    ]
