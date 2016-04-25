# -*- coding: utf-8 -*-
from django.shortcuts import render
 
 
def home2(request):
    string = u"Python 网站建设学习！Fightting"
    TutorialList = ["Html","Css","Python","Django","C++"]
    return render(request, 'vartest/home.html',{'TutorialList': TutorialList})