# Generated by Django 3.1.7 on 2021-03-26 11:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20210326_1154'),
    ]

    operations = [
        migrations.RenameField(
            model_name='movie',
            old_name='cast',
            new_name='price',
        ),
        migrations.RemoveField(
            model_name='movie',
            name='director',
        ),
        migrations.RemoveField(
            model_name='movie',
            name='release_date',
        ),
    ]