#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.shortcuts import render
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
    HostList = Asset.objects.filter(HostName__contains = name)
    print HostList
    for item in HostList:
        print item.HostName
    return HttpResponse('Ok')
