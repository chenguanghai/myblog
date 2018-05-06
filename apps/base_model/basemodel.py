from django.db import models

#自定义抽象模型类父类
class BaseModel(models.Model):
    create_time=models.DateTimeField(auto_now_add=True,verbose_name='创建时间')
    update_time=models.DateTimeField(auto_now=True,verbose_name='更新时间')
    is_delete=models.BooleanField(default=False,verbose_name='删除标记')

    class Meta:
        #抽象类，在迁移时不生成表
        abstract=True