# Generated by Django 3.1.2 on 2020-10-06 09:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0002_todo_image_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='image',
            field=models.ImageField(blank=True, upload_to='pictures'),
        ),
    ]