# Generated by Django 2.1.5 on 2019-01-20 08:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0007_send_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='send',
            name='status',
            field=models.CharField(blank=True, db_index=True, max_length=150),
        ),
        migrations.AlterField(
            model_name='send',
            name='task',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='tasks.Task'),
        ),
    ]
