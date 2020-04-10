#coding=utf-8
from django.db import models
from accounts.models import User
from django.db.models.deletion import CASCADE

# Create your models here.
class Order(models.Model):
    person = models.ForeignKey(User,on_delete=CASCADE)
    platform = models.CharField(max_length = 20)
    start_date = models.DateField('开始日期',null=True)
    end_date = models.DateField('结束日期',null=True)
    found_date = models.DateField('创建日期')
    delete_date = models.DateField('删除日期',null=True)
    unit = models.CharField(max_length=20,null=True)#单位
    receiver_id = models.CharField(max_length=20,null=True)
    recive_time = models.TimeField('签收日期',null=True)
    verifier_id = models.CharField(max_length=20,null=True)#审核员id
    recaller_id = models.CharField(max_length=20,null=True)#撤除人
    status_code = models.IntegerField(default=0)
    note = models.CharField(max_length=200,null=True)
    def creater(self):
        return User.objects.get(pk=self.person_id).name
    def verifier(self):
        if self.verifier_id:
            return User.objects.get(pk=self.verifier_id).name
        else:
            return ''
    def recaller(self):
        if self.recaller_id:
            return User.objects.get(pk=self.recaller_id).name
        else:
            return ''
    def startdate(self):
        if(self.start_date):
            return self.start_date.strftime("%Y-%m-%d")
        else:
            return '未填写'
    def enddate(self):
        if(self.end_date):
            return self.end_date.strftime("%Y-%m-%d")
        else:
            return '未填写'
    def founddate(self):
        return self.found_date.strftime("%Y-%m-%d")
    def deletedate(self):
        if(self.delete_date):
            return self.delete_date.strftime("%Y-%m-%d")
        else:
            return ''
    def status(self):
        status_code=self.status_code
        if status_code==0:
            return '未提交'
        elif status_code==1:
            return '审核中'
        elif status_code==2:
            return '未通过'
        elif status_code==3:
            return '待发布'
        elif status_code==4:
            return '发布成功'
        elif status_code==5:
            return '已撤除'
        else:
            return 'erro'
    
class Order_item(models.Model):
    order = models.ForeignKey(Order,on_delete=CASCADE)
    start_time = models.DateTimeField('开始时间')
    end_time = models.DateTimeField('结束时间')
    place = models.CharField(max_length=50)
    cause = models.CharField(max_length=20)
    speed_limit = models.IntegerField(default=100)
    speed_note = models.CharField(max_length=100,null=True)
    pattern = models.CharField(max_length=100)
    device = models.CharField(max_length=100)