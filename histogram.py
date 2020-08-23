# -*- coding: utf-8 -*-
# @Time    : 2020-07-06 15:27
# @Author  : chenshiyang
# @Email   : chenshiyang@blued.com
# @File    : histogram.py           画柱图
# @Software: PyCharm

import numpy as np
from matplotlib import pyplot as plt
from matplotlib.font_manager import FontProperties
import pymysql
import matplotlib as mpl

conn = pymysql.connect('10.9.128.47', 'root', 'qatest', 'HttpRunner', charset='utf8')
cur = conn.cursor()
# sql查询语句
# sql = "select author,count(1) from `TestCaseInfo` GROUP BY author;;"# 人员对对应接口
sql = "SELECT b.module_name,count(a.belong_module_id) FROM TestCaseInfo a LEFT JOIN ModuleInfo b ON a.belong_module_id = b.id GROUP BY a.belong_module_id;"# 模块对应接口
# noinspection PyBroadException
try:
    # 执行sql语句
    cur.execute(sql)
    # 取得上个查询的结果，是单个结果
    result = cur.fetchall()
except BaseException as e:
    # 发生错误时回滚
    print('111',e)
    conn.rollback()
    conn.close()

labels = [i[0] for i in result]

# 包含每个柱子对应值的序列
sizes = [i[1] for i in result]
print(labels,sizes)

font = FontProperties(fname='/Library/Fonts/Songti.ttc', size=5)

# 创建一个点数为 8 x 6 的窗口, 并设置分辨率为 80像素/每英寸
plt.figure(figsize=(8,6), dpi=200)

# 再创建一个规格为 1 x 1 的子图
plt.subplot(1, 1, 1)

# 柱子总数
N = len(labels)

# 包含每个柱子下标的序列
index = list(np.arange(N))
print('index',index)

# 柱子的宽度
width = 0.8

# 绘制柱状图, 每根柱子的颜色为紫罗兰色
p2 = plt.bar(index, sizes, width, label="接口数", color="lightgreen")


# 设置横轴标签
plt.xlabel('name')
# 设置纵轴标签
plt.ylabel('count')

# 添加标题
plt.title('国内国际模块对应接口数',fontproperties=font,fontsize=16)

# 添加纵横轴的刻度
plt.xticks(index, labels,fontproperties=font)
plt.xticks(rotation=270)
plt.yticks(np.arange(0,400,50))

# 添加图例
plt.legend(prop=font)
plt.savefig('/Users/danlan/Documents/p4.png',dpi=200)
plt.show()