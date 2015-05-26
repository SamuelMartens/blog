# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0006_auto_20150508_1235'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='post_eval',
        ),
        migrations.AddField(
            model_name='post',
            name='comments_num',
            field=models.PositiveIntegerField(default=0),
            preserve_default=True,
        ),
    ]
