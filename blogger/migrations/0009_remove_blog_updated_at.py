# Generated by Django 3.0.7 on 2020-06-18 04:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogger', '0008_auto_20200618_0732'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='updated_at',
        ),
    ]
