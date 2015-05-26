# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0012_auto_20150519_1711'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userimage',
            name='user_to',
        ),
        migrations.DeleteModel(
            name='UserImage',
        ),
    ]
