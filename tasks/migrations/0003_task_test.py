# Generated by Django 2.1.5 on 2019-01-19 17:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0002_test'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='test',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='tasks.Test'),
            preserve_default=False,
        ),
    ]