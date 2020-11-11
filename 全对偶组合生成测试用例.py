# -*- coding: utf-8 -*-
# @Time    : 2020-07-28 15:19
# @Author  : chenshiyang
# @Email   : chenshiyang@blued.com
# @File    : 全对偶组合生成测试用例.py
# @Software: PyCharm

import itertools
import json
import time

from allpairspy import AllPairs


test = """{
    "a": [{"a": "string"}],
    "b": ["string"],
    "c": "string",
    "d": "bool",
    "e": "int",
    "f": {"ff": "string", "gg": "int"}
}"""

# 同样 设定 范围值，每一种参数有几个取值范围，进行覆盖测试
# 1对偶算法覆盖
# 2全覆盖（笛卡尔积算法）


def get_data_list(_type, request_type=0):
    """
    0表示对偶算法；1表示全匹配组合
    返回参数的取值范围
    """
    if _type == 'string':
        return ["", None, "abc123"]
    elif _type == 'time':
        return ["1900-01-01",
                time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())]
    elif _type == 'int':
        return [-1, 0, 1]
    elif _type == 'decimal':
        return [-0.50, 0.0, 0.50]
    elif _type == 'bool':
        return [True, False]
    elif isinstance(_type, dict):
        if request_type == 0:
            return dual_test_case(_type)
        elif request_type == 1:
            return itertools_case_list(_type)
    elif isinstance(_type, list):
        new_list = []
        c_list = []
        if isinstance(_type[0], dict):   # 字典集合,递归取得自己的取值范围
            if request_type == 0:
                c_list = dual_test_case(_type[0])  # 对偶算法
            elif request_type == 1:
                c_list = itertools_case_list(_type[0])  # 全匹配算法
            for case in c_list:
                new_list.append([case])
        else:  # 数组集合
            v_list = get_data_list(_type[0])
            for case in v_list:
                new_list.append([case])
            new_list.append(v_list)  # 补全一下多个值的数组
        return new_list


def all_assemble(dic):
    """返回每个参数的取值范围组成的二维数据，用于求笛卡尔积"""
    return_list = []
    for k, v in dic.items():
        k_list = []
        for _value in get_data_list(v, 1):
            di = dict()
            di[k] = _value
            k_list.append(di)
        return_list.append(k_list)
    return return_list


def itertools_case_list(dic):
    """笛卡尔积"""
    _list = all_assemble(dic)
    case_list = []
    for item in itertools.product(*_list):
        d3 = {}
        for di in item:
            d3.update(di)
        case_list.append(d3)
    return case_list


def dual_test_case(_base):
    """对偶生成测试用例"""
    if not isinstance(_base, dict):
        return []
    key_list = list()
    value_list = list()
    case_list = list()

    for k, v in _base.items():
        key_list.append(k)
        value_list.append(get_data_list(v))

    print(key_list)
    print('value_list---', value_list)

    if value_list.__len__() >= 2:
        res = AllPairs(value_list)
        for i, b in enumerate(res):
            # print i, b
            dic = dict()
            for n in range(b.__len__()):
                dic[key_list[n]] = b[n]
            case_list.append(dic)
    else:
        for v in value_list[0]:
            dic = dict()
            dic[key_list[0]] = v
            case_list.append(dic)
    return case_list


# 测试一下
case_list1 = dual_test_case(json.loads(test))
print(case_list1.__len__())
for case in case_list1:
    print(str(json.dumps(case)))
# case_list2 = itertools_case_list(json.loads(test))
# print(case_list2.__len__())
# for case in case_list2:
#     print(str(json.dumps(case)))
