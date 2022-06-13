# Generated by Django 3.2.11 on 2022-03-30 11:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_guidebooking'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cars',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('seats', models.ImageField(upload_to='')),
                ('large_bag', models.IntegerField()),
                ('small_bag', models.IntegerField()),
                ('mileage', models.CharField(max_length=200)),
                ('price', models.IntegerField()),
                ('image', models.ImageField(upload_to='images/')),
            ],
        ),
    ]