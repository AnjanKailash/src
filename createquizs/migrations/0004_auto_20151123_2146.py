# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('createquizs', '0003_auto_20151123_2135'),
    ]

    operations = [
        migrations.CreateModel(
            name='qstns',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('question', models.CharField(max_length=200)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('right_choice', models.CharField(max_length=200)),
                ('marks', models.IntegerField(default=1)),
                ('category', models.ForeignKey(to='createquizs.category')),
            ],
        ),
        migrations.RemoveField(
            model_name='choice',
            name='question',
        ),
        migrations.RemoveField(
            model_name='question',
            name='category',
        ),
        migrations.DeleteModel(
            name='choice',
        ),
        migrations.DeleteModel(
            name='question',
        ),
    ]
