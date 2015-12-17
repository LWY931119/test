# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('btApp', '0002_data'),
    ]

    operations = [
        migrations.AlterField(
            model_name='data',
            name='data',
            field=models.FloatField(),
        ),
    ]
