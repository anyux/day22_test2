#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "anyux"
# Date: 2018/11/5

from django.shortcuts import redirect,render,HttpResponse
from login.models import User

def list(request):
    my_list = User.objects.all()
    return render(request,"list.html",locals())
