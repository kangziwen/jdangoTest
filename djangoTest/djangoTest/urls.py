"""djangoTest URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
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
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib import staticfiles
from django.conf.urls import url,include
from django.contrib import admin
from  app_name import views
from app01 import views as views1
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    # url(r'^index',views.index),
    url(r'^login',views1.login),
    url(r'^index', views1.index),
    url(r'^logout', views1.logout),
    url(r'^user/', include('app02.urls')),
    url(r'^model/', include('app_name.urls')),

]
#设置静态文件路径
urlpatterns += staticfiles_urlpatterns()