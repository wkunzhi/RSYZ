from django.shortcuts import render, HttpResponse


# Create your views here.

def index(request):
    """首页"""
    return render(request, 'index.html')


def about_me(request):
    """关于作者"""
    return render(request, 'about_me.html')


def strategy(request):
    """攻略"""
    return render(request, 'strategy.html')
