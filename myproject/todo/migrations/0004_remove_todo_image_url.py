# Generated by Django 3.0.5 on 2020-10-08 15:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0003_todo_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='todo',
            name='image_url',
        ),
    ]