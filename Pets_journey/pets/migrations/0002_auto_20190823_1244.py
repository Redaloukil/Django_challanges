# Generated by Django 2.1.1 on 2019-08-23 12:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pets', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cat',
            name='breed',
        ),
        migrations.RemoveField(
            model_name='dog',
            name='breed',
        ),
    ]
