# -*- coding: utf-8 -*-
# @Time    : 2020-06-20 08:55
# @Author  : chenshiyang
# @Email   : chenshiyang@blued.com
# @File    : 文件读写.py
# @Software: PyCharm

"""
假设你正在编写的方法，需要每次执行时，在服务器上创建一个临时文件书写部分内容，而后将该文件的对象传输给第三方的函数，待第三方获取到你文本内的数据，最后执行对该临时文件的删除操作。请在纸上完善代码：

import os

def three_func(file_object=None):
    data = file_object.read()
    final_data = data.decode() if isinstance(data, bytes) else data
    print(f'read file info:{final_data}')

def make_temp_file():
 ...
    # call three_func
    three_func(_tmp_file)
 ...

make_temp_file()
"""

import os
import tempfile


def three_func(file_object=None):
    data = file_object.read()
    final_data = data.decode() if isinstance(data, bytes) else data
    print(f'read file info:{final_data}')

def make_temp_file():
    _tmp_file = tempfile.TemporaryFile()
    try:
        _tmp_file.write(b'something')
        _tmp_file.seek(0)
        three_func(_tmp_file)
    finally:
        _tmp_file.close()

make_temp_file()

"""
流式读取数G超大文件
使用with...open...可以从一个文件中读取数据，但是如果你使用不当，也会带来很大的麻烦。
比如当你使用了read函数，其实Python会将文件的内容一次性的全部载入内存中，如果文件有10个G甚至更多，那么你的电脑消耗的内存非常巨大。
"""

# 一次性读取
with open('big_file.txt', 'r') as fp:
    content = fp.read()

# 逐行读取返回（使用生成器）
def read_from_file(filename):
    with open(filename, 'r') as fp:
        yield fp.readline()


# 如果文件只有一行，一行就10个G，还是会一次性读取全部内容，最优雅的解决方法是，在使用read方法时，指定每次只读取固定大小的内容
def read_from_file(filename, block_size = 1024 * 8):
    with open(filename, 'r') as fp:
        while True:
            chunk = fp.read(block_size) # 读取指定大小，每次读取8kb
            if not chunk:
                break
            yield chunk

