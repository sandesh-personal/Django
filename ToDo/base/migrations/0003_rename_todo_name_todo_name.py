# Generated by Django 4.2.4 on 2023-08-23 08:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_remove_todo_name_todo_todo_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='todo',
            old_name='todo_name',
            new_name='name',
        ),
    ]