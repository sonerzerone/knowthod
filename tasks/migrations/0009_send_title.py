# Generated by Django 2.1.5 on 2019-01-20 09:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0008_auto_20190120_1154'),
    ]

    operations = [
        migrations.AddField(
            model_name='send',
            name='title',
            field=models.CharField(db_index=True, default='', max_length=150),
            preserve_default=False,
        ),
    ]
