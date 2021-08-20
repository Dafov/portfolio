# Generated by Django 3.2.6 on 2021-08-17 15:16

import django.contrib.postgres.functions
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio_projects', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='id',
            field=models.UUIDField(default=django.contrib.postgres.functions.RandomUUID, editable=False, primary_key=True, serialize=False, unique=True),
        ),
    ]
