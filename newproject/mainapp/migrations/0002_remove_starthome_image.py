# Generated by Django 4.1.3 on 2022-12-01 15:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='starthome',
            name='image',
        ),
    ]