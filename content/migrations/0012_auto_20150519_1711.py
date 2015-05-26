# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0011_postimage_userimage'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='postimage',
            name='post_to',
        ),
        migrations.DeleteModel(
            name='PostImage',
        ),
    ]
