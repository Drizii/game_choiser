# Generated by Django 3.0.3 on 2020-02-23 18:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='choose',
            field=models.BooleanField(default=False),
        ),
    ]