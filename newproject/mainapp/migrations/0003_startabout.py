# Generated by Django 4.1.3 on 2022-12-01 17:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0002_remove_starthome_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Startabout',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('text', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'Start about',
                'verbose_name_plural': 'Start about',
            },
        ),
    ]
