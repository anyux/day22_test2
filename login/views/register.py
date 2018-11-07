#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "anyux"
# Date: 2018/11/4

from django.shortcuts import redirect,HttpResponse,render
from login.forms.user import UserModelForm
from login.models import User

def register(request):
    title_login = "欢迎注册"
    title_password = "密码"
    title_user = "用户名"
    form = UserModelForm()
    if request.method == "GET":
        return render(request,"register.html",locals())
    else:
        form = UserModelForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('/login/login/')

        return render(request,"register.html",locals())
