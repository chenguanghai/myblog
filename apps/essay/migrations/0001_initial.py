# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Eassay',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('is_delete', models.BooleanField(default=False, verbose_name='删除标记')),
                ('title', models.CharField(max_length=30, verbose_name='文章标题')),
                ('content', tinymce.models.HTMLField(max_length=9999, default='', null=True, verbose_name='文章详情', blank=True)),
                ('image', models.ImageField(upload_to='essay_title', verbose_name='文章图片')),
                ('status', models.SmallIntegerField(default=0, choices=[(0, 1)], verbose_name='文章状态')),
                ('likenum', models.IntegerField(default=0, verbose_name='点赞数')),
                ('readnum', models.IntegerField(default=0, verbose_name='阅读数')),
            ],
            options={
                'verbose_name': '文章',
                'verbose_name_plural': '文章',
                'db_table': 'bg_essay',
            },
        ),
        migrations.CreateModel(
            name='EssayImage',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('is_delete', models.BooleanField(default=False, verbose_name='删除标记')),
                ('image', models.ImageField(upload_to='essay', verbose_name='文章内容图片')),
            ],
            options={
                'verbose_name': '文章内容图片',
                'verbose_name_plural': '文章内容图片',
                'db_table': 'bg_essay_image',
            },
        ),
        migrations.CreateModel(
            name='EssayTalk',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('is_delete', models.BooleanField(default=False, verbose_name='删除标记')),
                ('content', tinymce.models.HTMLField(max_length=640, verbose_name='文章评论')),
                ('essay', models.ForeignKey(to='essay.Eassay', verbose_name='文章')),
            ],
            options={
                'verbose_name': '文章评论',
                'verbose_name_plural': '文章评论',
                'db_table': 'bg_essay_talk',
            },
        ),
        migrations.CreateModel(
            name='Kind',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('is_delete', models.BooleanField(default=False, verbose_name='删除标记')),
                ('name', models.CharField(max_length=20, verbose_name='种类名称')),
            ],
            options={
                'verbose_name': '文章分类',
                'verbose_name_plural': '文章分类',
                'db_table': 'bg_essay_kind',
            },
        ),
    ]
