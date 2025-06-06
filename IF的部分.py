# -*- coding: utf-8 -*-
"""
Created on Fri Jun  6 09:46:12 2025

@author: frogk
"""

sex = input("你是男的女的(M/F):")
weight = eval(input("請輸入體重(kg):"))
height = eval(input("請輸入身高(cm):"))

bmi = weight/(height/100)**2

if sex == 'M':
    if bmi > 25:
        print("死肥宅")
    elif bmi < 21:
        print("竹竿人")
    else:
        print("帥哥")
        
else:
    if bmi > 22:
        print("死胖子")
    elif bmi < 19:
        print("人乾")
    else:
        print("辣妹")