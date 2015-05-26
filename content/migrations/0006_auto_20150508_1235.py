# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0005_auto_20150506_1837'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='comm_cont',
            field=models.TextField(max_length=400),
            preserve_default=True,
        ),
    ]
