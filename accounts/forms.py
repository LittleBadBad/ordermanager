#coding=utf-8
'''
Created on 2020年3月14日

@author: zcy
'''
from django.forms import widgets
from django import forms  # 导入表单模块
from accounts.models import User
import re,base64,hashlib

class logForm(forms.Form):
    phone = forms.CharField(label='手机号',widget=forms.TextInput(attrs={"class": "vTextField"}))
    password = forms.CharField(label='密码',widget=forms.PasswordInput(attrs={"class": "vTextField"}))
#     def clean_phone(self):
#         phone=self.cleaned_data.get('phone')
#         if not User.objects.filter(phone=phone).exists():
#             raise forms.ValidationError('此号码不存在')
#         else:
#             return phone
    def clean(self):
        phone=self.cleaned_data.get('phone')
        password=self.cleaned_data.get('password')
        phone = base64.b64encode(phone.encode('utf-8'))
        phone = str(phone,'utf-8')
        try:
            user = User.objects.get(phone=phone)
        except User.DoesNotExist:
            self.add_error('phone', '此号码不存在')
            raise forms.ValidationError('error')
        if hashlib.sha1(password.encode('utf-8')).hexdigest() == user.password:
            return self.cleaned_data
        else:
            self.add_error('password', '密码错误')
            


class regForm(forms.Form): # 自定义表单类，并继承forms.Form
    username = forms.CharField(
        max_length=20,
        label='用户名',
        widget=forms.TextInput(attrs={"class": "vTextField"})
    )
    CHECKBOX_CHOICES = (
         (0,'调度员'),
         (1,'审核员'),
         (2,'管理员'),
         (3,'值班员')
         )
    telephone = forms.CharField(
        max_length=11,
        label='电话',
        widget=widgets.TextInput(attrs={'class': 'vTextField'}))
    password = forms.CharField(
        min_length=6,
        label='密码',
        widget=forms.PasswordInput(attrs={"class": "vTextField"}))
    password2 = forms.CharField(
        min_length=6,
        label='再次输入',
        widget=forms.PasswordInput(attrs={"class": "vTextField"}))
    state = forms.ChoiceField(
        label='身份',
        choices=CHECKBOX_CHOICES,
        widget=forms.Select(attrs={"class": "vTextField"}))
    station = forms.CharField(
        max_length=20,
        label='车站',
        widget=forms.TextInput(attrs={"class": "vTextField"}),
        required=False
        )
    def clean_password(self):# 自定义方法（局部钩子），密码必须包含字母和数字
        password=self.cleaned_data.get('password')
        if password.isdigit() or password.isalpha():
            raise forms.ValidationError('密码必须包含数字和字母')
        else:
            return self.cleaned_data['password']
    def clean_telephone(self):
        telephone=self.cleaned_data.get('telephone')
        if not len(telephone) == 11:
            raise forms.ValidationError("格式错误！")
        else:
            telephone = base64.b64encode(telephone.encode('utf-8'))
            telephone = str(telephone,'utf-8')
            if User.objects.filter(phone=telephone).exists():
                raise forms.ValidationError('此号码已注册，是否找回？')
            else:
                return self.cleaned_data['telephone']
    def clean(self): # 自定义方法（全局钩子, 检验两个字段），检验两次密码一致;
        if self.cleaned_data.get('password') != self.cleaned_data.get('password2'):
            self.add_error('password2', '密码不一致')
            raise forms.ValidationError('密码不一致')
        else:
            return self.cleaned_data