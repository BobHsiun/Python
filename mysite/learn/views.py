#coding:utf-8
from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse(u"欢迎光临 Python学习!!!!!!!!!!")

def home(request):
    return render(request,"home.html")
