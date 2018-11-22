from django.db import models
from db.base_model import BaseModel
from group.models import Group
from user.models import User


class Wish(BaseModel):

    status_choices = (
        (0, "待抽取"),
        (1, "待完成"),
        (2, "已完成"),
        (3, "已取消"),
    )
    name = models.CharField(max_length=20, verbose_name='愿望名称')
    desc = models.CharField(max_length=256, verbose_name='愿望详情')
    group = models.ForeignKey('Group', on_delete=models.CASCADE, verbose_name='所属分组')
    create_user = models.ForeignKey('User', on_delete=models.CASCADE, verbose_name='创建者')
    value = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='愿望价值')
    weight = models.SmallIntegerField(default=1, choices=(0, 10), verbose_name="愿望权重")
    status = models.SmallIntegerField(default=0, choices=status_choices, verbose_name='愿望状态')
    end_time = models.DateTimeField(verbose_name='截止时间')

    class Meta:
        db_table = 'wl_wish'
        verbose_name = '愿望'
        verbose_name_plural = verbose_name
