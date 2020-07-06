# -*- coding: utf-8 -*-
# @Time    : 2020-06-22 23:52
# @Author  : chenshiyang
# @Email   : chenshiyang@blued.com
# @File    : 闭包.py
# @Software: PyCharm

def func(a, b):
    def inner(x):
        nonlocal a # 使用nonlocal关键字，改变外函数中局部变量的值，如果外函数中没有a变量，此处会报位置错误
        a = 3
        return a + b + x
    return inner

s = func(1,5)
print(s(6))

