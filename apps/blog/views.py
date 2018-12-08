from django.shortcuts import render
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage  # 分页及没有页码和超出页码try提示

from apps.blog.models import *
from RSYZ import settings


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


def strategy_list(request, obj_id, page_num):
    """具体攻略列表"""
    if request.method == 'GET':

        name = StrategyClass.objects.filter(id=obj_id)[0].title  # 板块大标题
        obj_list = StrategyArticle.objects.filter(strategyClass=obj_id).order_by('create_time')  # 取所有文章对象，按发布时间正序排
        tag_list = Tag.objects.all()  # 取标签，便于渲染颜色

        '''分页器'''
        paginator_obj = Paginator(obj_list, settings.STRATEGY_LIST_NUM)  # 实例化分页器对象，设置每页n条,最有一页少于n条就合并到上一页
        cont_page = paginator_obj.num_pages
        now_num = int(page_num)

        '''固定显示5个页码,当前页码在中间'''
        if paginator_obj.num_pages > 5:
            if now_num - 2 < 1:
                page_range = range(1, 6)
            elif now_num + 3 > paginator_obj.num_pages:
                page_range = range(paginator_obj.num_pages-4, paginator_obj.num_pages+1)
            else:
                page_range = range(now_num - 2, now_num + 3)
        else:
            page_range = paginator_obj.page_range

        # 页码异常
        try:
            page_obj = paginator_obj.page(page_num)  # 当前分页对象
        except PageNotAnInteger:
            page_obj = paginator_obj.page(1)  # 输入不是数字 返回1页
        except EmptyPage:
            page_obj = paginator_obj.page(paginator_obj.num_pages)  # 页码超出 就放最后一页(取最大页数)

        return render(request, 'strategy_list.html', locals())


def strategy_article(request, article_id):
    """攻略文章"""
    if request.method == 'GET':
        obj = StrategyArticle.objects.filter(pk=article_id).first()
        # 阅读次数统计
        count = obj.read_count
        obj.read_count = count + 1
        obj.save()
        return render(request, 'strategy_article.html', locals())
