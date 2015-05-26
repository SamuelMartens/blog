# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0004_auto_20150506_1815'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='comm_cont',
            field=models.TextField(max_length=1000),
            preserve_default=True,
        ),
    ]
