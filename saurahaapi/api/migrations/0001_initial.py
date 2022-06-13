# Generated by Django 3.2.11 on 2022-02-23 06:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Accomodation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Accommodation_name', models.CharField(max_length=200)),
                ('Accommodation_type', models.CharField(max_length=200)),
                ('location', models.CharField(max_length=200)),
                ('price', models.IntegerField()),
                ('discount', models.IntegerField()),
                ('image', models.ImageField(upload_to='')),
            ],
        ),
    ]
