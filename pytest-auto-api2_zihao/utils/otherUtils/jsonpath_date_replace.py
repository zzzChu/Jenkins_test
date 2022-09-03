#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2022/5/23 18:27
# @Author  : 余少琪
# @Email   : 1603453211@qq.com
# @File    : jsonpath_date_replace
# @describe:

def jsonpath_replace(change_data, key_name):
    """处理jsonpath数据"""
    _new_data = key_name + ''
    for i in change_data:
        if i == '$':
            pass
        elif i[0] == '[' and i[-1] == ']':
            _new_data += "[" + i[1:-1] + "]"
        else:
            _new_data += "[" + "'" + i + "'" + "]"
    return _new_data
