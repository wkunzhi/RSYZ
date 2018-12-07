from django.contrib import admin
from .models import *


class StrategyClassConfig(admin.ModelAdmin):
    """定制攻略主题"""
    list_filter = ['title', 'type']
    list_display = ['title', 'type']


class StrategyArticleConfig(admin.ModelAdmin):
    """定制攻略文章"""
    list_filter = ['title', 'read_count', 'strategyClass']
    list_display = ['title', 'read_count', 'strategyClass']


class TagConfig(admin.ModelAdmin):
    """定制攻略标签"""
    list_display = ['title']


admin.site.register(StrategyClass, StrategyClassConfig)
admin.site.register(StrategyArticle, StrategyArticleConfig)
admin.site.register(Tag, TagConfig)


