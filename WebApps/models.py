from __future__ import unicode_literals

from django.db import models

# Create your models here.

class UserType(models.Model):
    Type = models.CharField(max_length = 50)

class UserInfo(models.Model):
    username = models.CharField(max_length = 50)
    password = models.CharField(max_length = 50)
    Gender = models.BooleanField(default = False)
    Age = models.IntegerField(default = 18)
    Memo = models.TextField(default = 'Memo')
    CreateDate = models.DateField(default = '2016-10-01')
    CreateTime = models.DateTimeField(default = '2016-10-01 10:10:10')
    #One To Many
    Type = models.ForeignKey('UserType')

class Group(models.Model):
    GroupName = models.CharField(max_length = 50)

class User(models.Model):
    UserName = models.CharField(max_length = 50)
    Email = models.CharField(max_length = 50)
    #Many To Many
    GroupRelation = models.ManyToManyField('Group')
    #One To One

class Args(models.Model):
    Name = models.CharField(max_length = 50, null = True)
    Pass = models.CharField(max_length = 50, null = False)

class Asset(models.Model):
    HostName = models.CharField(max_length = 50)
    CreateDate = models.DateTimeField(auto_now_add = True)
    UpdateDate = models.DateTimeField(auto_now = True)

class Sex(models.Model):
    GENDER_CHOICE = (
        (u'1', u'User'),
        (u'2', u'Admin'),
        (u'3', u'SuperAdmin')
    )
    UserType = models.CharField(max_length = 20, choices = GENDER_CHOICE)
