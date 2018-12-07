"""RSYZ URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path

# media配置 打开该路径浏览器访问权限
from django.views.static import serve

from RSYZ import settings
from apps.blog import views

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path('^$', views.index),  # 首页
    path('about_me/', views.about_me),  # 作者页


    # media配置
    re_path(r'media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),

    # 攻略区
    path('strategy/', views.strategy),  # 攻略首页
    re_path('strategy/(?P<name>\w+)$', views.strategy_list),  # 对应攻略列表


]
