# Generated by Django 3.1.3 on 2020-12-18 13:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mumbai', '0002_auto_20201126_1411'),
    ]

    operations = [
        migrations.CreateModel(
            name='booking',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('age', models.IntegerField()),
                ('date', models.DateTimeField()),
            ],
        ),
        migrations.RemoveField(
            model_name='bookingtrain',
            name='option',
        ),
        migrations.RemoveField(
            model_name='bookingtrain',
            name='user',
        ),
        migrations.DeleteModel(
            name='bookingflight',
        ),
        migrations.DeleteModel(
            name='bookingtrain',
        ),
        migrations.DeleteModel(
            name='flightoptions',
        ),
        migrations.DeleteModel(
            name='trainoptions',
        ),
    ]
