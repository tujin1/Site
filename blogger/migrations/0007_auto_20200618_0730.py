# Generated by Django 3.0.7 on 2020-06-18 04:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogger', '0006_auto_20200618_0729'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, verbose_name='update timestamp'),
        ),
    ]