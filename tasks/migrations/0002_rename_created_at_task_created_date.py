# Generated by Django 5.0.4 on 2025-03-13 14:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='created_at',
            new_name='created_date',
        ),
    ]
