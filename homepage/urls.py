#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @Project : studio
# @FileName  :homepage.url.py
# @Time      :2023/4/22 0:01
# @Author    :和孔哥一起学
# @Email     :2338199895@qq.com
# @CSDN and Public      :和孔哥一起学

from django.urls import path
from homepage.views import *

urlpatterns = [
    path('', index, name='index'),
    path('index/', index, name='index'),
    path('contact/', contact, name='contact'),
    path('AiSecurity/', AiSecurity, name='AiSecurity'),
    path('AiEducate/', AiEducate, name='AiEducate'),
    path('AiAgriculture/', AiAgriculture, name='AiAgriculture'),
    path('AiFinance/', AiFinance, name='AiFinance'),
    path('AiMedical/', AiMedical, name='AiMedical'),
    path('AiHousehold/', AiHousehold, name='AiHousehold'),
]
