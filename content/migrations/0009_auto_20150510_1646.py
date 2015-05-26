# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0008_auto_20150510_1644'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='comments_num',
            field=models.PositiveIntegerField(default=2),
            preserve_default=True,
        ),
    ]
