# -*- coding: utf-8 -*
from . import models
import time

#定时任务，更新订单状态为已完成
def test():
    cu = time.strftime("%Y-%m-%d")
    li = []
    cu = cu.split('-')
    for i in cu:
        li.append(i)
    t = models.order.objects.filter(status=1, endtime__year=li[0], endtime__month=li[1], endtime__day=li[2])
    for i in t:
        if i.footposition!=None:
            models.order.objects.filter(footposition=i.footposition).update(status=3)

