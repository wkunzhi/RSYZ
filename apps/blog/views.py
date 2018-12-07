from django.shortcuts import render, HttpResponse

from apps.blog.models import *


def index(request):
    """首页"""
    return render(request, 'index.html')


def about_me(request):
    """关于作者"""
    return render(request, 'about_me.html')


def strategy(request):
    """攻略"""
    if request.method == 'GET':
        type1_list = StrategyClass.objects.filter(type='1')
        type2_list = StrategyClass.objects.filter(type='2')
        return render(request, 'strategy.html', locals())


def strategy_list(request, name):
    """具体攻略列表"""
    if request.method == 'GET':
        return render(request, 'strategy_list.html', locals())