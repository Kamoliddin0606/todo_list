# Generated by Django 4.0.6 on 2022-08-06 11:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_alter_todolist_end_time_alter_todolist_start_time'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='todolist',
            name='status',
        ),
        migrations.AddField(
            model_name='todolist',
            name='progress',
            field=models.BooleanField(default=False),
        ),
    ]
