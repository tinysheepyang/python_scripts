# -*- coding: utf-8 -*-
# @Time    : 2020-06-20 22:15
# @Author  : chenshiyang
# @Email   : chenshiyang@blued.com
# @File    : super.py
# @Software: PyCharm

"""
单继承
在单继承时，super().__init__()与Base.__init__()是一样的。super()避免了基类的显式调用
"""

class Base:
    def __init__(self):
        print('Create Base')


class A(Base):
    def __init__(self):
        # Base.__init__(self)
        # super(A, self).__init__() # Python2
        super().__init__() # Python3
        print('Create A')

# A()

"""
多继承
super于父类没有实质性的关联，在单继承时，super获取的类刚好是父类，在多继承时，super获取的是继承顺序中的下一个类。以下面的继承方式为例：
  Base
  /  \
 /    \
A      B
 \    /
  \  /
   C
"""

class Base:
    def __init__(self):
        print ("enter Base")
        print ("leave Base")

class A(Base):
    def __init__(self):
        print ("enter A")
        super().__init__()
        print ("leave A")

class B(Base):
    def __init__(self):
        print ("enter B")
        super().__init__()
        print ("leave B")

class C(A, B):
    def __init__(self):
        print ("enter C")
        super().__init__()
        print ("leave C")

# C()
print(C.mro())

"""
使用Base().__init__ 方式
"""

class A1(Base):
    def __init__(self):
        print ("enter A")
        Base().__init__()
        print ("leave A")

class B1(Base):
    def __init__(self):
        print ("enter B")
        Base().__init__()
        print ("leave B")

class C1(A1, B1):
    def __init__(self):
        print ("enter C")
        A1().__init__()
        B1().__init__()
        print ("leave C")

# C1()
print(C1.mro())

"""
从上面看到，不使用super 基类会多次被调用，开销非常大

对于定义的类，在Python中会创建一个MRO(Method Resolution Order)列表，它代表了类继承的顺序。查看MRO列表：


从测试结果来看，两种方式的MRO列表是一样的。MRO的查找顺序(python3)是按广度优先来的(基类继承object，Python2是深度优先)
super的好处是避免直接使用父类的名字(隐式调用)，主要用于多层继承
避免使用 super(self.__class__, self)
"""