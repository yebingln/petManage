from django.db import models

class UserInfo(models.Model):
    telephone=models.IntegerField()
    password=models.CharField()