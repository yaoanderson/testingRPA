#!/usr/bin/env python
# coding=utf8

"""
-------------------------------------------------
   File Name:     policy
   Description:
   Author:        anderson
   date:          2019-11-25
-------------------------------------------------
"""

import random


class Policy(object):

    @classmethod
    def apply_policies(cls, value_lines, range_list, min_length):
        cls.append_null_val(value_lines)
        cls.append_min_val(value_lines, range_list, min_length)
        cls.append_smaller_than_min_val(value_lines, range_list, min_length)

    # scenario #1
    @classmethod
    def append_null_val(cls, value_lines):
        value_lines.append("null, ")

    # scenario #2
    @classmethod
    def append_min_val(cls, value_lines, range_list, min_length):
        # generate all chars
        _temp_str = ""
        for i in range(min_length):
            _temp_str += random.choice(range_list)
        value_lines.append(_temp_str + ", ")

    # scenario #3
    @classmethod
    def append_smaller_than_min_val(cls, value_lines, range_list, min_length):
        # generate part of chars
        _temp_str = ""
        for i in range(random.randint(1, min_length - 1)):
            _temp_str += random.choice(range_list)
        value_lines.append(_temp_str + "\n")
