#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "anyux"
# Date: 2018/11/4

from django.shortcuts import redirect,HttpResponse,render
from login.forms.user import UserModelForm

def login(request):
    title_login = "欢迎登陆"
    title_password = "密码"
    title_user = "用户名"
    form = UserModelForm()
    if request.method == "POST":
        form = UserModelForm(data=request.POST)
        if form.is_valid():
            return HttpResponse("登陆成功")
    return render(request,"login.html",locals())
