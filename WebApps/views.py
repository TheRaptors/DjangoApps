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
