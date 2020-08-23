# -*- coding: utf-8 -*-
# @Time    : 2020-07-06 15:28
# @Author  : chenshiyang
# @Email   : chenshiyang@blued.com
# @File    : drawing.py             画饼图
# @Software: PyCharm



from matplotlib import pyplot as plt
from matplotlib.font_manager import FontProperties
import pymysql

conn = pymysql.connect('10.9.128.47', 'root', 'qatest', 'HttpRunner', charset='utf8')
cur = conn.cursor()
# sql查询语句
sql = "select belong_project,count(1) from `TestCaseInfo` GROUP BY belong_project;"
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
sizes = [i[1] for i in result]

print(labels,sizes)
font = FontProperties(fname='/Library/Fonts/Songti.ttc', size=12)
plt.figure(figsize=(6, 9))  # 调节图形大小

colors = ['yellowgreen', 'lightgreen', 'darkgreen', 'gold', 'red', 'lightsalmon', 'darkred','purple','orange','hotpink']  # 每块颜色定义
explode = (0, 0.02, 0, 0,0,0.02,0,0,0,0.01)  # 将某一块分割出来，值越大分割出的间隙越大
patches, text1, text2 = plt.pie(sizes,
                                explode=explode,
                                labels=labels,
                                colors=colors,
                                labeldistance=1.2,  # 图例距圆心半径倍距离
                                autopct='%3.2f%%',  # 数值保留固定小数位
                                shadow=False,  # 无阴影设置
                                startangle=90,  # 逆时针起始角度设置
                                pctdistance=0.8)  # 数值距圆心半径倍数距离
# patches饼图的返回值，texts1饼图外label的文本，texts2饼图内部文本

for t in text1:
    t.set_fontproperties(font)  # 把每个文本设成中文字体


# x，y轴刻度设置一致，保证饼图为圆形
plt.axis('equal')
plt.legend(prop=font)  # 图例也显示中文
plt.savefig('/Users/danlan/Documents/p2.png',dpi=600)  # 一定放在plt.show()之前
plt.show()
