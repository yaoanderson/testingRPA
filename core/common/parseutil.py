#!/usr/bin/env python
# coding=utf8

"""
-------------------------------------------------
   File Name:     parseutil
   Description:
   Author:        anderson
   date:          2019-11-25
-------------------------------------------------
"""

import configparser


class ConfigParser(object):
    CONF = configparser.ConfigParser()

    @classmethod
    def read_config(cls, path):
        cls.CONF.read(path)

    @classmethod
    def get_section(cls, section):
        return cls.CONF.options(section)

    @classmethod
    def get_option(cls, section, option):
        return cls.CONF.get(section, option)
