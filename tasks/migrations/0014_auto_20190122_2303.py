# Generated by Django 2.1.5 on 2019-01-22 20:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0013_remove_test_test'),
    ]

    operations = [
        migrations.AlterField(
            model_name='test',
            name='input',
            field=models.CharField(db_index=True, max_length=1000),
        ),
        migrations.AlterField(
            model_name='test',
            name='output',
            field=models.CharField(db_index=True, max_length=1000),
        ),
    ]
