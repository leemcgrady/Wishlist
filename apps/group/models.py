# from django.db import models
# from db.base_model import BaseModel
# from user.models import User
#
# class Group(BaseModel):
#     '''分组模型类'''
#
#     group_name = models.CharField(max_length=20, verbose_name='分组名称')
#     desc = models.CharField(max_length=256, verbose_name='分组简介')
#     # image = models.ImageField(upload_to='goods', verbose_name='分组图片')
#
#     class Meta:
#         db_table = 'wl_group'
#         verbose_name = '分组'
#         verbose_name_plural = verbose_name
#
#
# class GroupUser(BaseModel):
#
#     '''分组用户模型类'''
#
#     status_choices = (
#         (0, '下线'),
#         (1, '上线'),
#     )
#     group = models.ForeignKey('Group', on_delete=models.CASCADE, verbose_name='所属组')
#     user_id = models.ForeignKey('User', on_delete=models.CASCADE, verbose_name='用户id')
#
#     status = models.SmallIntegerField(default=1, choices=status_choices, verbose_name='用户状态')
#
#     class Meta:
#         db_table = 'wl_group_user'
#         verbose_name = '分组用户'
#         verbose_name_plural = verbose_name