# Generated by Django 3.0.7 on 2020-06-18 05:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogger', '0013_remove_blog_updated_at'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='username',
        ),
    ]
