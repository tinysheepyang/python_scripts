# -*- coding: utf-8 -*-
# @Time    : 2020-09-17 16:33
# @Author  : chenshiyang
# @Email   : chenshiyang@blued.com
# @File    : test.py
# @Software: PyCharm

from redis import StrictRedis


redis = StrictRedis(host='10.9.126.228', port=6379, db=0)


import csv
with open('/Users/danlan/Downloads/foo.csv','r',encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        # 读取出的内容是列表格式的
        print(row,type(row),row[1])
        redis.hset(f'live:activity:happy:week:20200914:u:{row[1]}', 'task_count', 10000000000)