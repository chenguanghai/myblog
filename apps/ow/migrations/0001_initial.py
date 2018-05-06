# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ContactMe',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('is_delete', models.BooleanField(default=False, verbose_name='删除标记')),
                ('weibo_url', models.URLField(verbose_name='微博地址')),
                ('wechat_qrcode', models.ImageField(upload_to='station_contactme', verbose_name='微信二维码')),
                ('qq_qrcode', models.ImageField(upload_to='station_contactme', verbose_name='qq二维码')),
            ],
            options={
                'verbose_name': '联系我',
                'verbose_name_plural': '联系我',
                'db_table': 'bg_contactme',
            },
        ),
        migrations.CreateModel(
            name='StationAdvise',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('is_delete', models.BooleanField(default=False, verbose_name='删除标记')),
                ('eamil', models.EmailField(max_length=254, verbose_name='邮箱')),
                ('content', tinymce.models.HTMLField(max_length=9999, verbose_name='建议内容')),
            ],
            options={
                'verbose_name': '站点建议',
                'verbose_name_plural': '站点建议',
                'db_table': 'bg_station_advise',
            },
        ),
        migrations.CreateModel(
            name='StationInfo',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('is_delete', models.BooleanField(default=False, verbose_name='删除标记')),
                ('visitor_num', models.IntegerField(verbose_name='访问量')),
            ],
            options={
                'verbose_name': '站点信息',
                'verbose_name_plural': '站点信息',
                'db_table': 'bg_station_info',
            },
        ),
        migrations.CreateModel(
            name='VisitorInfo',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('is_delete', models.BooleanField(default=False, verbose_name='删除标记')),
                ('visitor_ip', models.GenericIPAddressField(verbose_name='ip地址')),
                ('visitor_browser', models.CharField(max_length=32, verbose_name='浏览器类型')),
                ('visitor_system', models.CharField(max_length=20, verbose_name='系统')),
            ],
            options={
                'verbose_name': '游客信息',
                'verbose_name_plural': '游客信息',
                'db_table': 'bg_visitor_info',
            },
        ),
    ]
