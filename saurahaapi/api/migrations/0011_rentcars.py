# Generated by Django 3.2.11 on 2022-03-31 12:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0010_alter_cars_seats'),
    ]

    operations = [
        migrations.CreateModel(
            name='RentCars',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('seats', models.IntegerField()),
                ('large_bag', models.IntegerField()),
                ('small_bag', models.IntegerField()),
                ('mileage', models.CharField(max_length=200)),
                ('price', models.IntegerField()),
                ('image', models.ImageField(upload_to='images/')),
                ('email', models.EmailField(max_length=200, unique=True)),
            ],
        ),
    ]
