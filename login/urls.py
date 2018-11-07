#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "anyux"
# Date: 2018/11/4

from django.urls import path,re_path
from login.views import login
from login.views import register
from login.views import list
from login.views import delete
from login.views import edit

urlpatterns = [
    path('login/',login.login),
    path('register/',register.register),
    path('list/',list.list),
    re_path('delete/(?P<nid>\d+)/',delete.delete),
    re_path('edit/(?P<nid>\d+)/',edit.edit),
]

