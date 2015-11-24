# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('createquizs', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='createquiz',
            name='date_added',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
