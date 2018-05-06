from django.db import models

# Create your models here.
from tinymce.models import HTMLField

from apps.base_model.basemodel import BaseModel


class ContactMe(BaseModel):
    """联系我模型类"""
    weibo_url=models.URLField(verbose_name='微博地址')
    wechat_qrcode=models.ImageField(upload_to='station_contactme',verbose_name='微信二维码')
    qq_qrcode=models.ImageField(upload_to='station_contactme',verbose_name='qq二维码')

    class Meta:
        db_table='bg_contactme'
        verbose_name='联系我'
        verbose_name_plural=verbose_name

class StationAdvise(BaseModel):
    """站点建议"""
    eamil=models.EmailField(verbose_name='邮箱')
    content=HTMLField(max_length=9999,verbose_name='建议内容')

    class Meta:
        db_table='bg_station_advise'
        verbose_name='站点建议'
        verbose_name_plural=verbose_name

class StationInfo(BaseModel):
    """站点信息"""
    visitor_num=models.IntegerField(verbose_name='访问量')

    class Meta:
        db_table='bg_station_info'
        verbose_name='站点信息'
        verbose_name_plural=verbose_name

class VisitorInfo(BaseModel):
    """游客信息模型类"""
    visitor_ip=models.GenericIPAddressField(verbose_name='ip地址')
    visitor_browser=models.CharField(max_length=32,verbose_name='浏览器类型')
    visitor_system=models.CharField(max_length=20,verbose_name='系统')

    class Meta:
        db_table='bg_visitor_info'
        verbose_name='游客信息'
        verbose_name_plural=verbose_name


