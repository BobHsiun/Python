# -*- coding: utf-8 -*-
from django.shortcuts import render
 
 
def home2(request):
    string = u"Python 网站建设学习！Fightting"
    TutorialList = ["Html","Css","Python","Django","C++"]
    info_dict = map(str, range(5))# 一个长度为100的 List
    return render(request, 'vartest/home.html',{'info_dict': info_dict})