# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['pub_date']},
        ),
        migrations.AlterField(
            model_name='post',
            name='post_cont',
            field=models.TextField(),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='post',
            name='theme',
            field=models.CharField(max_length=60),
            preserve_default=True,
        ),
    ]
