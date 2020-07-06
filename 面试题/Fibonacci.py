# -*- coding: utf-8 -*-
# @Time    : 2020-06-19 11:10
# @Author  : chenshiyang
# @Email   : chenshiyang@blued.com
# @File    : Fibonacci.py  集中求斐波那契数列n项和的方式
# @Software: PyCharm

from functools import lru_cache
import timeit


def fib(n):
    """
    递归法求斐波那契n项和，写法最简洁、效率最低，会出现大量的重复计算，时间复杂度O（1.618^n）,而且最深度1000
    :param n:
    :return:
    """

    assert isinstance(n, int)

    if n < 2:
        return n

    return fib(n - 2) + fib(n - 1)


print('递归---', timeit.timeit(lambda: fib(10), number=1))


def fib1(n):
    """
    递增法求斐波那契数列，时间复杂度是 O(n)，呈线性增长，如果数据量巨大，速度会越拖越慢
    :param n:
    :return:
    """

    assert isinstance(n, int)

    if n < 2:
        return n

    a = 0
    b = 1

    for i in range(n - 1):
        a, b = b, a + b

    return b


print('递增---', timeit.timeit(lambda: fib1(10), number=1))


def fib2(n):
    """
    生成器实现，返回值不是一个列表而是一个生成器，可以通过for in 或者next()来获取
    :param n:
    :return:
    """
    assert isinstance(n, int)

    if n < 2:
        return n

    a = 0
    b = 1

    while n > 0:
        a, b = b, a + b
        n -= 1
        yield a

# for i in fib2(10):
#     print(i)


class Fib:
    """
    通过魔术方法实现
    """

    def __init__(self, n):
        self.n = n
        self.current = 0
        self.a = 0
        self.b = 1

    def __next__(self):
        """当使用for in 或者next()时就可以调用下一个数"""
        if self.current < self.n:
            self.a, self.b = self.b, self.a + self.b
            self.current += 1
            return self.a
        else:
            raise StopIteration

    def __iter__(self):
        return self


# fib = Fib(10)
# for i in fib:
#     print(i)


"""
for循环的本质是通过不断调用next()函数实现的

    for x in [1, 2, 3, 4, 5]:
        pass
相当于:

    # 首先获取可迭代对象
    it = iter([1, 2, 3, 4, 5])
    # while next
    while True:
        try:
            next(it)
        except StopIteration:
            # 遇到StopIteration就退出循环
            break
"""


@lru_cache(None)
def fib3(n):
    """
    递归求斐波那契数列使用缓存
    :param n:
    :return:
    """
    assert isinstance(n, int)

    if n < 2:
        return n

    return fib3(n - 2) + fib3(n - 1)


print('使用缓存---', timeit.timeit(lambda: fib3(500), number=1))


def fib4(n):
    """
    闭包，从历史记录中查找避免重复计算
    :param n:
    :return:
    """
    assert isinstance(n, int)
    if n < 2:
        return n

    dict1 = {}
    dict1[0] = 0
    dict1[1] = 1

    def f(m):
        if m not in dict1:
            dict1[m] = f(m - 2) + f(m - 1)
        return dict1[m]

    return f(n)


print('闭包1---', timeit.timeit(lambda: fib4(10), number=1))


def f2(func):
    cache = {}
    cache[0] = 0
    cache[1] = 1

    def wrap(*args):
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]
    return wrap


@f2
def fib5(n):
    assert isinstance(n, int)
    if n < 2:
        return n

    return fib5(n - 1) + fib5(n - 2)


print('闭包2---', timeit.timeit(lambda: fib5(10), number=1))

"""
总结：
1.使用缓存lru_cache,速度最快
2.递归效率最低、递增速度最慢
3.闭包速度不稳定
4.生成器最节省空间
"""
