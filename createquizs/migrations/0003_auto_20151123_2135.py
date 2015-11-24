# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('createquizs', '0002_auto_20151123_2037'),
    ]

    operations = [
        migrations.CreateModel(
            name='question',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('question_text', models.CharField(max_length=200)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('right_choice', models.CharField(max_length=200)),
                ('marks', models.IntegerField(default=1)),
                ('category', models.ForeignKey(to='createquizs.category')),
            ],
        ),
        migrations.RemoveField(
            model_name='createquiz',
            name='category',
        ),
        migrations.AlterField(
            model_name='choice',
            name='question',
            field=models.ForeignKey(to='createquizs.question'),
        ),
        migrations.DeleteModel(
            name='createquiz',
        ),
    ]
