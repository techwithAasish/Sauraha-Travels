# Generated by Django 3.2.11 on 2022-02-24 10:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_alter_accomodation_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accomodation',
            name='image',
            field=models.ImageField(upload_to=''),
        ),
    ]