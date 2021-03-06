# Generated by Django 2.1.3 on 2018-11-22 12:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('group', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Wish',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('is_delete', models.BooleanField(default=False, verbose_name='删除标记')),
                ('name', models.CharField(max_length=20, verbose_name='愿望名称')),
                ('desc', models.CharField(max_length=256, verbose_name='愿望详情')),
                ('value', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='愿望价值')),
                ('weight', models.SmallIntegerField(default=1, verbose_name='愿望权重')),
                ('status', models.SmallIntegerField(choices=[(0, '待抽取'), (1, '待完成'), (2, '已完成'), (3, '已取消')], default=0, verbose_name='愿望状态')),
                ('end_time', models.DateTimeField(verbose_name='截止时间')),
                ('create_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='创建者')),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='group.Group', verbose_name='所属分组')),
            ],
            options={
                'verbose_name_plural': '愿望',
                'verbose_name': '愿望',
                'db_table': 'wl_wish',
            },
        ),
    ]
