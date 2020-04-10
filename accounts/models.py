#coding=utf-8
from django.db import models

# Create your models here.
import hashlib
import base64
from django.utils import timezone

class User(models.Model):
    name = models.CharField(max_length=20)
    password = models.CharField(max_length=128)
    phone = models.CharField(max_length=50)
    state = models.IntegerField(default=0)
    reg_time = models.DateTimeField('注册日期')
    def save(self, *args, **kwargs):#override save function
        #print('0',self.phone)
        self.password = hashlib.sha1(self.password.encode('utf-8')).hexdigest()
        self.phone = base64.b64encode(self.phone.encode('utf-8'))
        self.phone = str(self.phone,'utf-8')
        now=timezone.now()
        self.reg_time=now
        #print('1',self.phone)
        super(User, self).save(*args, **kwargs)
    def statename(self):
        if self.state == 0:
            return ''
        elif self.state == 1:
            return '审核员'
        elif self.state == 2:
            return '管理员'
        else:
            return 'erro'
    def __str__(self):
        #print('2',self.phone)
        phone_decode=base64.b64decode(self.phone)
        #print(phone_decode)
        phone_decode=str(phone_decode,'utf-8')
        #print(phone_decode)
        return self.name + ' ' + phone_decode