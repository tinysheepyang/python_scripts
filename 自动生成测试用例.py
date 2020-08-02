# -*- coding: utf-8 -*-
# @Time    : 2020-07-28 15:17
# @Author  : chenshiyang
# @Email   : chenshiyang@blued.com
# @File    : 自动生成测试用例.py
# @Software: PyCharm

import copy
import time

dic1 = """{
"a": [{"aa": "string"}],
"b": ["string"],
"c": "string",
"d": "bool",
"e": "int",
"f": {"ff": "string", "gg": "int"}
}"""
# 需要对每一个参数做基础验证，比如说string类型的参数传"",NULL，特殊字符，超长字符等等
# 需要对每个参数依次替换，生成对应的测试用例
#
# 先指定每个类型的需要测试的范围
def get_type_base_value(_type):
    """根据类型获取基础测试的值"""
    if _type == 'string':
        #  string类型测试，空，NULL，特殊字符，脚本，正常字符，超长字符
        return ["", None, "!@#$%^&*()_+<>?:{}|~`", "<JavaScript>alert(0)</JavaScript>", "test_string","qwertyuiooasdfghjklzxcvbnmazxwsedrtfrrfugyyyfyhjjjkgughsdjgagfjdbdbsddkakdfhakjnnnnnnnnnnnnnkjguyy234567iujwertyuiosdfghjkxcvbmsdfghjkqwertyuizxcvbnasdfghjwertyui234tydfgcvdfrc c1qaz2wsx3edc4rfv5tgb6yhn7ujm8ik9ol0pqwertyuiopdfghjklzxcvbnm"]
    elif _type == 'time':
        #  时间类型测试 错误的年，月，日，非时间类值, 当前时间
        return ["0000-01-01", "1600-01-01", "2010-13-30", "2010-02-30", "not_time", time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())]
    elif _type == 'int':
        #  整型测试 非数字类型，溢出, 0
        return ["not_int", 12567890123456781234567123451234567, -12345678912345678912345678901234567, 0]
    elif _type == 'decimal':
        #  浮点测试 非数字类型，溢出, 0
        return ["not_decimal", 12567890123456781234567123451234567.88, -12345678912345678912345678901234567.50, 0.00]
    elif _type == 'bool':
        #  布尔类型 非布尔类型, True, False
        return ["not_bool", True, False]
    else:
        #  递归方法
        return recursive_case(_type)


#然后开始替换参数值
def create_base_case(_source):
    return_list = []
    for k, v in _source.items():
        for _value in get_type_base_value(v):
            dic_cp2 = copy.deepcopy(_source)
            dic_cp2[k] = _value
            return_list.append(dic_cp2)     #  改成 return_list.append(replace_default(dic_cp2))   非测试参数替换成替换默认值
    return return_list

# 简单类型都被替换了，复杂类型则需要递归替换里面的参数


def recursive_case(_type):
    """递归,返回特殊类型的取值范围"""
    if isinstance(_type, list):
        new_list = []
        if isinstance(_type[0], dict):
            t_value_list = create_base_case(_type[0])  # 基础测试用例设计
            for t_value in t_value_list:
                new_list.append([t_value])
        else:
            for _value in get_type_base_value(_type[0]):
                new_list.append([_value])
        return new_list
    elif isinstance(_type, dict):
        return create_base_case(_type)
    else:
        return [None]

# 除却需要测试的值，其他类型全部替换成默认值
def replace_default(dic):
    """替换成默认值"""
    for k, v in dic.items():
        if isinstance(v, list):
            if isinstance(v[0], dict):
                dic[k] = [replace_default(v[0])]
            else:
                dic[k] = [default_value(v[0])]
        elif isinstance(v, dict):
            dic[k] = replace_default(v)
        else:
            dic[k] = default_value(v)
    return dic


def default_value(_type):
    if _type == 'string':
        return "default_string"
    elif _type == 'time':
        return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    elif _type == 'int':
        return 0
    elif _type == 'decimal':
        return 0.00
    elif _type == 'bool':
        return True
    else:
        return _type


dic1 = {'online':'bool', 'weight': 'int', 'condition': 'bool', 'height':'int',
        'age':'int', 'is_vip':'bool', 'geo_reach':'int', 'has_avatar':'bool','time_span':'int'}

# 测试一下
case_list2 = create_base_case(dic1)
print(len(case_list2))
for case in case_list2:
    print(case)