# Generated by Django 4.1.3 on 2022-12-02 12:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0005_startteam_delete_startabout'),
    ]

    operations = [
        migrations.CreateModel(
            name='Startportfolio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='media/Start porfolio')),
                ('number', models.CharField(max_length=50)),
                ('text', models.CharField(max_length=500)),
            ],
            options={
                'verbose_name': 'Portfolio',
                'verbose_name_plural': 'Portfolio',
            },
        ),
    ]
