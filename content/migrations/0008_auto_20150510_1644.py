# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0007_auto_20150510_1638'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='comments_num',
            field=models.PositiveIntegerField(),
            preserve_default=True,
        ),
    ]
