# Generated by Django 2.1.5 on 2019-01-22 19:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0012_test_test'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='test',
            name='test',
        ),
    ]