# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('btApp', '0005_data_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Datas',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=30)),
                ('data', models.FloatField()),
                ('time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
