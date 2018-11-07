#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "anyux"
# Date: 2018/11/5

from django.shortcuts import redirect,render,HttpResponse
from login.models import User
from login.forms.user import UserModelForm

def edit(request,nid):
    obj = User.objects.filter(id=nid).first()
    form = UserModelForm(instance=obj)
    if request.method == "POST":
        form = UserModelForm(data=request.POST,instance=obj)
        if form.is_valid():
            form.save()
            return redirect('/login/list/')
    return render(request,'edit.html',locals())
