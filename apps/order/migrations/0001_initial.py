# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('is_delete', models.BooleanField(default=False, verbose_name='删除标记')),
                ('order_id', models.CharField(max_length=32)),
                ('trande_no', models.CharField(max_length=64, verbose_name='交易号')),
                ('pay_method', models.SmallIntegerField(default=2, choices=[(1, '银联支付'), (2, '支付宝支付'), (3, '微信支付')], verbose_name='支付方式')),
                ('prive', models.IntegerField(verbose_name='金钱')),
                ('coins', models.IntegerField(verbose_name='CGH币')),
            ],
            options={
                'verbose_name': '订单',
                'verbose_name_plural': '订单',
                'db_table': 'bg_order',
            },
        ),
    ]
