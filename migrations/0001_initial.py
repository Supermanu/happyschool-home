# Generated by Django 2.2.19 on 2021-04-01 09:17

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('core', '0012_auto_20201209_1955'),
    ]

    operations = [
        migrations.CreateModel(
            name='HomeSettingsModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('layout', django.contrib.postgres.fields.jsonb.JSONField(verbose_name='Layout of the home page')),
                ('teachings', models.ManyToManyField(default=None, to='core.TeachingModel')),
            ],
        ),
    ]
