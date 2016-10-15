#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http.response import HttpResponse
from WebApps.models import Asset

# Create your views here.

def index(request):
    return HttpResponse('index')

def login(request):
    return HttpResponse('login')

def list(request, id, Ghost):
    print id, Ghost
    return HttpResponse('list')

def Add(request, name):
    Asset.objects.create(HostName = name)
    return HttpResponse('Ok')

def Del(request, id):
    Asset.objects.get(id = id).delete()
    return HttpResponse('Ok')

def Update(request, id, name):
    Obj = Asset.objects.get(id = id)
    Obj.HostName = name
    Obj.save()
    return HttpResponse('Ok')

#批量更新，if id > value
def UPdate(request, id, name):
    Asset.objects.filter(id__gt = id).update(HostName = name)
    return HttpResponse('Ok')

def Get(request, name):
    #返回包含关键字的记录
    '''
    HostList = Asset.objects.filter(HostName__contains = name)
    print HostList
    for item in HostList:
        print item.HostName
    return HttpResponse('Ok')
    '''

    #返回所有记录
    '''
    AllData = Asset.objects.all()
    print AllData.query
    print AllData
    return HttpResponse('Ok')
    '''
    
    #返回所有记录，只取id,HostName字段
    AllData = Asset.objects.all().values('id','HostName')
    print AllData.query
    print AllData
    return HttpResponse('Ok')
    
    #返回前两条记录
    '''
    AllData = Asset.objects.all()[0:2]
    print AllData.query
    print AllData
    return HttpResponse('Ok')
    '''
    
    #返回所有记录，按id倒序排列(PS:'id'为正序)
    '''
    AllData = Asset.objects.all().order_by('-id')
    #显示SQL语句
    print AllData.query
    for item in AllData:
        print item.id
    return HttpResponse('Ok')
    '''

def AssetList(request):
    AssetList = Asset.objects.all()

    return render_to_response('AssetList.html', {'data':AssetList, 'user':'Ghost'})


def Login(request):
    if request.method == "POST":
        UserName = request.POST.get('USERNAME', None)
        Password = request.POST.get('PASSWORD', None)
        print UserName, Password
        return render_to_response('Login.html')
    else:
        return render_to_response('Login.html')
