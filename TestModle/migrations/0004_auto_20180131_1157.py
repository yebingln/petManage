# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-01-31 11:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TestModle', '0003_auto_20180131_0623'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='cashfinish',
            field=models.CharField(choices=[(1, '是'), (2, '否')], default=1, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='creat_date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='frequency',
            field=models.CharField(choices=[(1, '天/次'), (2, '周/次'), (2, '月/次')], default=1, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='update_data',
            field=models.DateTimeField(auto_now=True, error_messages={'invalid': '日期格式错误'}, null=True),
        ),
        migrations.AlterField(
            model_name='position',
            name='footposition',
            field=models.CharField(choices=[(1, '1号食物柜'), (2, '2号食物柜'), (3, '3号食物柜'), (4, '4号食物柜'), (5, '5号食物柜'), (6, '6号食物柜')], default=1, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='position',
            name='petposition',
            field=models.CharField(choices=[(1, '1号房'), (2, '2号房'), (3, '3号房'), (4, '4号房'), (5, '5号房'), (6, '6号房')], default=1, max_length=50, null=True),
        ),
    ]
