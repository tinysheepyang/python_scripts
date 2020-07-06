# -*- coding: utf-8 -*-
# @Time    : 2020-06-22 22:24
# @Author  : chenshiyang
# @Email   : chenshiyang@blued.com
# @File    : for循环的实现原理.py
# @Software: PyCharm

"""
for循环是对容器进行迭代的过程，什么是迭代?,迭代就是从容器对象中逐个读取元素，直到容器对象中元素读完为止

哪些对象支持迭代操作？
可迭代对象需要实现__iter__方法,并返回一个迭代器

什么是迭代器？
实现了__next__方法

for循环实现原理？
1.判断对象是否是可迭代对象，不是可迭代对象直接报错，抛出TypeError异常，是可迭代对象则调用__iter__方法，返回迭代器对象
2.迭代器不断调用__next__方法，每次按序返回迭代器对象中的一个值
3.容器对象中没有更多元素，则报StopIteration异常
"""

class MyRange:
    def __init__(self, num):
        self.num = num
        self.i = 0

    def __iter__(self):
        """告诉解释器我是可以返回迭代器的，迭代器就是我自己，没有__iter__方法时MyRange是一个迭代器不是一个可迭代对象"""
        return self

    def __next__(self):
        if self.i < self.num:
            i = self.i
            self.i += 1
            return i
        else:
            raise StopIteration


for i in MyRange(3):
    print(i)

test = MyRange(3)
print(test.__next__())
print(test.__next__())
print(test.__next__())