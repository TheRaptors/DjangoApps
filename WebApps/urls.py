"""DjangoProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from WebApps.views import index, Add, Del, Update, UPdate, Get

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^index/', index),
    url(r'^Add/(?P<name>\d*)/$', Add),
    url(r'^Del/(?P<id>\d*)/$', Del),
    url(r'^Update/(?P<id>\d*)/(?P<name>\d*)/$', Update),
    url(r'^UPdate/(?P<id>\d*)/(?P<name>\w*)/$', UPdate),
    url(r'^Get/(?P<name>\w*)/$', Get),
]
