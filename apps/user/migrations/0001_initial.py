# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.contrib.auth.models
import django.core.validators
import django.utils.timezone
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0006_require_contenttypes_0002'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(null=True, verbose_name='last login', blank=True)),
                ('is_superuser', models.BooleanField(help_text='Designates that this user has all permissions without explicitly assigning them.', default=False, verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, verbose_name='username', unique=True, help_text='Required. 30 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=30, validators=[django.core.validators.RegexValidator('^[\\w.@+-]+$', 'Enter a valid username. This value may contain only letters, numbers and @/./+/-/_ characters.', 'invalid')])),
                ('first_name', models.CharField(max_length=30, verbose_name='first name', blank=True)),
                ('last_name', models.CharField(max_length=30, verbose_name='last name', blank=True)),
                ('email', models.EmailField(max_length=254, verbose_name='email address', blank=True)),
                ('is_staff', models.BooleanField(help_text='Designates whether the user can log into this admin site.', default=False, verbose_name='staff status')),
                ('is_active', models.BooleanField(help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', default=True, verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('is_delete', models.BooleanField(default=False, verbose_name='删除标记')),
                ('phone_num', models.IntegerField(verbose_name='手机号')),
                ('head_pic', models.ImageField(upload_to='user_head_pic', default='ow.Station.head_pic', verbose_name='用户头像')),
                ('coins', models.IntegerField(default=0, verbose_name='CGH币')),
                ('groups', models.ManyToManyField(verbose_name='groups', blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_query_name='user', to='auth.Group', related_name='user_set')),
                ('user_permissions', models.ManyToManyField(verbose_name='user permissions', blank=True, help_text='Specific permissions for this user.', related_query_name='user', to='auth.Permission', related_name='user_set')),
            ],
            options={
                'verbose_name': '用户',
                'verbose_name_plural': '用户',
                'db_table': 'bg_user',
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='GiveConis',
            fields=[
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('is_delete', models.BooleanField(default=False, verbose_name='删除标记')),
                ('give_no', models.CharField(primary_key=True, max_length=32, serialize=False, verbose_name='打赏号')),
                ('coins', models.IntegerField(verbose_name='打赏数量')),
                ('user_id', models.CharField(max_length=32, verbose_name='支付人id')),
                ('to_user', models.ForeignKey(to=settings.AUTH_USER_MODEL, verbose_name='接收人')),
            ],
            options={
                'verbose_name': '打赏',
                'verbose_name_plural': '打赏',
                'db_table': 'bg_user_give',
            },
        ),
        migrations.CreateModel(
            name='Inform',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('is_delete', models.BooleanField(default=False, verbose_name='删除标记')),
                ('title', models.CharField(max_length=30, verbose_name='通知标题')),
                ('content', models.CharField(max_length=320, verbose_name='通知内容')),
                ('status', models.SmallIntegerField(default=1, choices=[(1, '待发送'), (2, '已发送'), (3, '已查看'), (4, '已删除')], verbose_name='状态')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL, verbose_name='用户')),
            ],
            options={
                'verbose_name': '通知消息',
                'verbose_name_plural': '通知消息',
                'db_table': 'bg_user_inform',
            },
        ),
        migrations.CreateModel(
            name='ReceiveConis',
            fields=[
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('is_delete', models.BooleanField(default=False, verbose_name='删除标记')),
                ('receive_no', models.CharField(primary_key=True, max_length=32, serialize=False, verbose_name='收赏号')),
                ('coins', models.IntegerField(verbose_name='收赏数量')),
                ('from_user', models.CharField(max_length=32, verbose_name='支付人id')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL, verbose_name='接收人')),
            ],
            options={
                'verbose_name': '收赏',
                'verbose_name_plural': '收赏',
                'db_table': 'bg_user_receive',
            },
        ),
    ]
