# Generated by Django 3.2 on 2021-04-08 15:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='createjob',
            name='location',
            field=models.CharField(default='', max_length=100),
        ),
    ]
