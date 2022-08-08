# Generated by Django 3.1.3 on 2020-11-25 13:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travel', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='destination',
            old_name='heart',
            new_name='offer',
        ),
        migrations.AddField(
            model_name='destination',
            name='price',
            field=models.IntegerField(default=750),
            preserve_default=False,
        ),
    ]
