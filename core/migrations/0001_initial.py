# Generated by Django 4.0.6 on 2022-07-06 16:32

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Double',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('value', models.IntegerField()),
                ('double_value', models.IntegerField(blank=True)),
                ('date', models.DateTimeField(blank=True, default=datetime.datetime(2022, 7, 6, 16, 32, 1, 723528))),
            ],
        ),
    ]