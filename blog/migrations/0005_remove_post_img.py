# Generated by Django 3.2.13 on 2023-11-17 06:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_post_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='img',
        ),
    ]