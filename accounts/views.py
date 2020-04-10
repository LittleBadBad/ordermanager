#coding=utf-8
from django.shortcuts import render, get_object_or_404, redirect
from django.template.context_processors import request
from django.http.response import HttpResponse,HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from accounts.forms import regForm,logForm
from accounts.models import User
from django.contrib import messages
import hashlib,base64
import json

def login(request):
    if(request.method=='POST'):
        myform = logForm(request.POST)
        if(myform.is_valid()):            
            data = myform.cleaned_data
            #print(data)
            phone = base64.b64encode(data['phone'].encode('utf-8'))
            phone = str(phone,'utf-8')
            user = get_object_or_404(User,phone=phone)
            userid = user.id
            request.session['id']=userid
            return redirect('orders:index')
        else:
            #print(myform.errors,'ERROR')
            return render(request, 'accounts/index.html',locals())
    myform=logForm()
    return render(request, 'accounts/index.html',locals())

def register(request):
    if(request.method=='POST'):
        myform=regForm(request.POST)
        #print(locals())
        # 3.校验，is_valid如果是true表示校验成功（满足myform里的条件）,反之,校验失败
        if(myform.is_valid()):
            # myform.clean_data 表示校验通过的数据
            
            data = myform.cleaned_data
            print(data)
            user = User()
            user.name=data['username']
            user.password=data['password']
            user.phone=data['telephone']
            user.state=data['state']
            user.save()
            
            print(User.objects.all())
            return HttpResponse('success')
        else:
            #print('errors',myform.errors)
            #print(myform.cleaned_data)
            #校验失败的信息，myform.errors  可以当成一个字典，它是所有错误信息{name:[列表,]}
            # 每个字段.errors 是一个列表，表示每个字段的错误信息
            print(myform.errors,'ERROR')
            return render(request, 'accounts/register.html',locals())
    myform = regForm(request.POST)
    return render(request, 'accounts/register.html',locals())
