# Generated by Django 2.1.5 on 2019-01-13 13:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('compiler', '0008_auto_20190113_1553'),
    ]

    operations = [
        migrations.AlterField(
            model_name='solution',
            name='input',
            field=models.TextField(blank=True, db_index=True, max_length=3000),
        ),
    ]
