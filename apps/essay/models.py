from django.db import models
from apps.base_model.basemodel import BaseModel
from tinymce.models import HTMLField
# Create your models here.

class Eassay(BaseModel):
    """文章模型类"""
    title=models.CharField(max_length=30,verbose_name='文章标题')
    kind=models.ForeignKey('Kind',verbose_name='种类')
    content=HTMLField(max_length=9999,blank=True,null=True,default='',verbose_name='文章详情')
    user=models.ForeignKey('user.User',verbose_name='用户')
    image=models.ImageField(upload_to='essay_title',verbose_name='文章图片')
    status=models.SmallIntegerField(choices=((0,1),),default=0,verbose_name='文章状态')
    likenum=models.IntegerField(default=0,verbose_name='点赞数')
    readnum=models.IntegerField(default=0,verbose_name='阅读数')

    class Meta:
        db_table='bg_essay'
        verbose_name='文章'
        verbose_name_plural=verbose_name

class Kind(BaseModel):
    """文章种类模型类"""
    name=models.CharField(max_length=20,verbose_name='种类名称')

    class Meta:
        db_table='bg_essay_kind'
        verbose_name='文章分类'
        verbose_name_plural=verbose_name

class EssayImage(BaseModel):
    """文章内容图片模型类"""
    essay=models.ForeignKey('Eassay',verbose_name='文章')
    image=models.ImageField(upload_to='essay',verbose_name='文章内容图片')

    class Meta:
        db_table='bg_essay_image'
        verbose_name='文章内容图片'
        verbose_name_plural=verbose_name

class EssayTalk(BaseModel):
    """文章评论模型类"""
    essay=models.ForeignKey('Eassay',verbose_name='文章')
    user=models.ForeignKey('user.User',verbose_name='用户')
    content=HTMLField(max_length=640,verbose_name='文章评论')

    class Meta:
        db_table='bg_essay_talk'
        verbose_name='文章评论'
        verbose_name_plural=verbose_name



