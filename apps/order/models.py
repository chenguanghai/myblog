from django.db import models

# Create your models here.
from apps.base_model.basemodel import BaseModel


class Order(BaseModel):
    """订单模型类"""
    PAY_METHOD=(
        (1,'银联支付'),
        (2,'支付宝支付'),
        (3,'微信支付')
    )
    order_id=models.CharField(max_length=32)
    trande_no=models.CharField(max_length=64,verbose_name='交易号')
    user=models.ForeignKey('user.User',verbose_name='用户')
    pay_method=models.SmallIntegerField(choices=PAY_METHOD,default=2,verbose_name='支付方式')
    prive=models.IntegerField(verbose_name='金钱')
    coins=models.IntegerField(verbose_name='CGH币')

    class Meta:
        db_table='bg_order'
        verbose_name='订单'
        verbose_name_plural=verbose_name
