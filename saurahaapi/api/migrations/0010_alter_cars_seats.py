# Generated by Django 3.2.11 on 2022-03-30 11:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0009_cars'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cars',
            name='seats',
            field=models.IntegerField(),
        ),
    ]
