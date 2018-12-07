from django.shortcuts import render
from django.core.paginator import Paginator  # 分页

from apps.blog.models import *


def index(request):
    """首页"""
    return render(request, 'index.html')


def about_me(request):
    """关于作者"""
    return render(request, 'about_me.html')


def strategy(request):
    """攻略主页"""
    if request.method == 'GET':
        type1_list = StrategyClass.objects.filter(type='1')
        type2_list = StrategyClass.objects.filter(type='2')
        return render(request, 'strategy.html', locals())


def strategy_list(request, obj_id):
    """具体攻略列表"""
    if request.method == 'GET':
        name = StrategyClass.objects.filter(id=obj_id)[0].title
        obj_list = StrategyArticle.objects.filter(strategyClass=obj_id)
        for i in obj_list:
            print(i.id)
        tag_list = Tag.objects.all()

        return render(request, 'strategy_list.html', locals())


def strategy_article(request, obj_id, article_id):
    """攻略文章"""
    if request.method == 'GET':
        obj = StrategyArticle.objects.filter(pk=article_id).first()
        count = obj.read_count
        obj.read_count = count + 1
        obj.save()
        return render(request, 'strategy_article.html', locals())
