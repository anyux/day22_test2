#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "anyux"
# Date: 2018/11/5

from django.shortcuts import redirect,render,HttpResponse
from login.models import User

def delete(request,nid):
    User.objects.filter(id=nid).delete()
    return redirect('/login/list/')
