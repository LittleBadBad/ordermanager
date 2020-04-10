#coding=utf-8
from django.shortcuts import render,get_object_or_404
from accounts.models import User
from orders.models import Order,Order_item
import base64
from django.utils import timezone
import datetime,json
from django.core import serializers
from orders.forms import orderForm
from django.db.models import Q
from django.http import response
from django.http.response import HttpResponse
# Create your views here.

def index(request):
    userid=request.session.get('id')    
    #print(userid)
    user = get_object_or_404(User, pk=userid)
    
    if user.state == 0:
        orders = user.order_set.filter(~Q(status_code=-1))#~Q取反
        #orders = user.order_set.filter(Q(status_code=0)|Q(status_code=1))
    elif user.state == 1:
        orders = Order.objects.filter(Q(status_code=1)|Q(status_code=2)|Q(status_code=3))
    elif user.state == 2:
        orders = Order.objects.filter(Q(status_code=3)|Q(status_code=4)|Q(status_code=5))
    return render(request, 'orders/index.html',{'user':user,'orders':orders})

def order(request):
    userid=request.session.get('id')
    user = get_object_or_404(User, pk=userid)
    phone = base64.b64decode(user.phone)
    phone=str(phone,'utf-8')
    title='新建命令'
    
    order = user.order_set.create(platform='广西南宁铁路局',found_date =datetime.datetime.now(),unit="济南车务段")
    myorderform=orderForm({'platform':'广西南宁铁路局','unit':"济南车务段"})
    
    myorderitemformlist=[]
    myorderitemformlist.append(myorderform.orderitemForm())
    
    return render(request, 'orders/order.html',locals())

# def orderItem(request,formlist,orderid):
#     order=get_object_or_404(Order,pk=orderid)
#     orderitem=order.orderitem_set.create()

def save(request,orderid):
    print(request.POST)
    print(orderid)
    order=get_object_or_404(Order,pk=orderid)
    data = request.POST
    
    order.platform=data['platform']
    order.start_date=data['start_date']
    order.end_date=data['end_date']
    order.unit=data['unit']
    order.receiver_id=data['receiver']
    order.save()
    order.order_item_set.all().delete()
    length = len(data.getlist('start_time'))
    print(length)
    for i in range( len(data.getlist('start_time'))):
        print(i)
        order.order_item_set.create(
            start_time=data.getlist('start_time')[i],
            end_time=data.getlist('end_time')[i],
            place=data.getlist('place')[i],
            cause=data.getlist('cause')[i],
            speed_limit=data.getlist('speed_limit')[i],
            speed_note=data.getlist('speed_note')[i],
            pattern=data.getlist('pattern')[i],
            device=data.getlist('device')[i]
        )
    
    return HttpResponse("保存成功")

def delete(request):
    #print(request.POST)
    data = request.POST
    order=get_object_or_404(Order,pk = data['id'])
    order.status_code=-1
    order.save()
    return HttpResponse(1)

def edit(request,orderid):
    order=get_object_or_404(Order,pk=orderid)
    userid=request.session.get('id')   
    user=get_object_or_404(User, pk=userid)
    phone = base64.b64decode(user.phone)
    phone=str(phone,'utf-8')
    title='编辑命令'
    
    myorderform=orderForm({
        'platform':order.platform,
        'start_date':order.start_date,
        'end_date':order.end_date,
        'unit':order.unit,
        'receiver':order.receiver_id
        })
    #print(myorderform)
    items=order.order_item_set.all()
    print(order.note)
    myorderitemformlist=[]
    for item in items:
        myorderitemformlist.append(myorderform.orderitemForm({
            'start_time':item.start_time.strftime("%Y-%m-%dT%H:%m"),
            'end_time':item.end_time.strftime("%Y-%m-%dT%H:%m"),
            'place':item.place,
            'cause':item.cause,
            'speed_limit':item.speed_limit,
            'speed_note':item.speed_note,
            'pattern':item.pattern,
            'device':item.device
            }))
    
    return render(request, 'orders/order.html', locals())

def submit(request):
    data = request.POST
    order=get_object_or_404(Order,pk = data['id'])
    order.status_code=1
    order.save()
    return HttpResponse(1)

def checkorder(request,orderid):
    order=get_object_or_404(Order,pk=orderid)
    orderitemlist=order.order_item_set.all()
    
    createrid=order.person_id
    creater=get_object_or_404(User, pk=createrid)
    
    userid=request.session.get('id')   
    user=get_object_or_404(User, pk=userid)
    
    phone = base64.b64decode(creater.phone)
    phone=str(phone,'utf-8')
    
    if user.state==1:
        title='审核命令'
    elif user.state==2:
        title='检查发布'
    
    return render(request, 'orders/checkorder.html', locals())

def passorder(request):
    data=request.POST
    orderid=data['id']
    userid=request.session.get('id')
    
    order=get_object_or_404(Order,pk=orderid)
    
    if order.status_code==1 or order.status_code==2:
        order.verifier_id=userid
        order.status_code=3
        order.save()
        return HttpResponse(1)
    else:
        return HttpResponse('erro')
    
def reject(request,orderid):
    data=request.POST
    order=get_object_or_404(Order,pk=orderid)
    userid=request.session.get('id')
    if order.status_code==1 or order.status_code==2:
        order.verifier_id=userid
        order.status_code=2
        order.note=data['note']
        order.save()
        return HttpResponse(1)
    else:
        return HttpResponse('erro')
    
def publishorder(request):
    data=request.POST
    orderid=data['id']
    order=get_object_or_404(Order,pk=orderid)
    order.status_code=4
    order.save()
    return HttpResponse(1)
    
# # 将class转dict,以_开头的属性不要
# def props(obj):
#     pr = {}
#     for name in dir(obj):
#         value = getattr(obj, name)
#         if not name.startswith('__') and not callable(value) and not name.startswith('_'):
#             pr[name] = value
#     return pr
# # 将class转dict,以_开头的也要
# def props_with_(obj):
#     pr = {}
#     for name in dir(obj):
#         value = getattr(obj, name)
#         if not name.startswith('__') and not callable(value):
#             pr[name] = value
#     return pr
# # dict转obj，先初始化一个obj
# def dict2obj(obj,dict):
#     obj.__dict__.update(dict)
#     return obj