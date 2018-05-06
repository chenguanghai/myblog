# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('essay', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='essaytalk',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, verbose_name='用户'),
        ),
        migrations.AddField(
            model_name='essayimage',
            name='essay',
            field=models.ForeignKey(to='essay.Eassay', verbose_name='文章'),
        ),
        migrations.AddField(
            model_name='eassay',
            name='kind',
            field=models.ForeignKey(to='essay.Kind', verbose_name='种类'),
        ),
        migrations.AddField(
            model_name='eassay',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, verbose_name='用户'),
        ),
    ]
