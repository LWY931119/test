# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('btApp', '0004_co2_lig_moi_tem'),
    ]

    operations = [
        migrations.AddField(
            model_name='data',
            name='name',
            field=models.CharField(default=123, max_length=30),
            preserve_default=False,
        ),
    ]
