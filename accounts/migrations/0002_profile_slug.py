# Generated by Django 2.1.4 on 2019-01-08 17:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='slug',
            field=models.SlugField(blank=True, max_length=150, unique=True),
        ),
    ]
