from django.db import models

class Account(models.Model):
    telephone=models.CharField(max_length=50,null=True)
    password=models.CharField(max_length=50,null=True)
    username=models.CharField(max_length=50,null=True)

class UserInfo(models.Model):
    name=models.CharField(max_length=50,null=True)
    telephone=models.IntegerField()
    # password=models.CharField(max_length=50)
    adress=models.CharField(max_length=50,null=True)

class Pet(models.Model):
    petname=models.CharField(max_length=50,null=True)
    pettype = (
        (1, u'猫'),
        (2, u'狗'),
        (3, u'小宠'),
        (4, u'其他'),
    )

    type=models.CharField(max_length=10,choices=pettype,null=True)
    pethost=models.ForeignKey('UserInfo',related_name='pet_user',on_delete=models.CASCADE)
    like=models.CharField(max_length=200,null=True)
    photo=models.ImageField(null=True)

class order(models.Model):
    ortele=models.ForeignKey('UserInfo',related_name='order_user',on_delete=models.CASCADE)
    creat_date = models.DateTimeField(auto_now_add=True,null=True)
    update_data = models.DateTimeField(auto_now=True, error_messages={'invalid': '日期格式错误'},null=True)
    starttime=models.DateTimeField(null=True)
    endtime=models.DateTimeField(null=True)
    cancelreasion=models.CharField(max_length=100,null=True)
    finished = (
        (1, u'是'),
        (2, u'否'),
    )
    cashfinish=models.CharField(choices=finished,max_length=10,null=True)
    finishincome=models.CharField(max_length=50,null=True)
    fre = (
        (1, u'天/次'),
        (2, u'周/次'),
        (2, u'月/次'),
    )
    frequency=models.CharField(max_length=50,choices=fre,null=True)
    # ortele=models.ForeignKey('UserInfo')
class Income(models.Model):
    income=models.CharField(max_length=50,null=True)
    pay=models.CharField(max_length=50,null=True)
    paytime=models.DateTimeField(null=True)
    payreasion=models.CharField(max_length=50,null=True)
class position(models.Model):
    pet_po = (
        (1, u'1号房'),
        (2, u'2号房'),
        (3, u'3号房'),
        (4, u'4号房'),
        (5, u'5号房'),
        (6, u'6号房'),
    )
    petposition=models.CharField(max_length=50,choices=pet_po,default=1,null=True)
    foot_po = (
        (1, u'1号食物柜'),
        (2, u'2号食物柜'),
        (3, u'3号食物柜'),
        (4, u'4号食物柜'),
        (5, u'5号食物柜'),
        (6, u'6号食物柜'),
    )
    footposition=models.CharField(max_length=50,choices=foot_po,default=1,null=True)

