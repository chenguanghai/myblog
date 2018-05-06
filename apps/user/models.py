from django.db import models
from django.contrib.auth.models import AbstractUser
from apps.base_model.basemodel import BaseModel
# Create your models here.

class User(AbstractUser,BaseModel):
    """继承ｄｊａｎｇｏ自带Ｕｓｅｒ抽象类，继承自定义抽象模型类"""
    phone_num=models.IntegerField(verbose_name='手机号')
    head_pic=models.ImageField(upload_to='user_head_pic',default='ow.Station.head_pic',verbose_name='用户头像')
    coins=models.IntegerField(default=0,verbose_name='CGH币')

    class Meta:
        db_table='bg_user'
        verbose_name='用户'
        verbose_name_plural=verbose_name


class GiveConis(BaseModel):
    """打赏模型类"""
    give_no = models.CharField(max_length=32, primary_key=True, verbose_name='打赏号')
    coins = models.IntegerField(verbose_name='打赏数量')
    user_id = models.CharField(max_length=32,verbose_name='支付人id')
    to_user = models.ForeignKey('User', verbose_name='接收人')

    class Meta:
        db_table = 'bg_user_give'
        verbose_name = '打赏'
        verbose_name_plural = verbose_name


class ReceiveConis(BaseModel):
    """收到打赏模型类"""
    receive_no=models.CharField(max_length=32,primary_key=True,verbose_name='收赏号')
    coins=models.IntegerField(verbose_name='收赏数量')
    user=models.ForeignKey('User',verbose_name='接收人')
    from_user=models.CharField(max_length=32,verbose_name='支付人id')

    class Meta:
        db_table='bg_user_receive'
        verbose_name='收赏'
        verbose_name_plural=verbose_name


class Inform(BaseModel):
    """通知模型类"""
    STATUS=(
        (1,'待发送'),
        (2,'已发送'),
        (3,'已查看'),
        (4,'已删除')
    )
    title=models.CharField(max_length=30,verbose_name='通知标题')
    content=models.CharField(max_length=320,verbose_name='通知内容')
    user=models.ForeignKey('User',verbose_name='用户')
    status=models.SmallIntegerField(choices=STATUS,default=1,verbose_name='状态')

    class Meta:
        db_table='bg_user_inform'
        verbose_name='通知消息'
        verbose_name_plural=verbose_name


