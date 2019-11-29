#!/usr/bin/env python
# coding=utf8

"""
-------------------------------------------------
   File Name:     case
   Description:
   Author:        anderson
   date:          2019-11-26
-------------------------------------------------
"""

from core.common.parseutil import ConfigParser
from core.case.config import Config

from mako.template import Template
import os


class Case(object):
    category = ""  # ui or api
    func = ""
    factor_list = []

    output_root = os.path.join(os.getcwd(), "output")
    case_root = os.path.join(os.getcwd(), "user")
    case_template_root = os.path.join(case_root, "case/template")
    case_config_root = os.path.join(case_root, "config")

    # manual case
    @classmethod
    def generate_manual_case(cls, dlist):
        pass

    # automation case
    @classmethod
    def generate_automation_case(cls, dlist):
        pass

    @classmethod
    def run(cls):
        # parse case config
        ConfigParser.read_config(os.path.join(cls.case_config_root, "%s_%s.ini" % (cls.category, cls.func)))
        # generate pict input and output file
        case_pict_file = os.path.join(cls.case_config_root, "%s_%s.txt" % (cls.category, cls.func))
        Config.generate_pict_input_file(case_pict_file)
        pict_output_list = Config.generate_pict_output_list(case_pict_file)

        cls.factor_list = Config.get_pict_output_factor_list(pict_output_list)
        data_list = Config.get_pict_output_data_list(pict_output_list)
        cls.generate_manual_case(data_list)
        cls.generate_automation_case(data_list)


class UICase(Case):
    category = "ui"
    page = ""

    # ui manual case
    @classmethod
    def generate_manual_case(cls, dlist):
        _template = Template(filename=os.path.join(cls.case_template_root, "%s-%s.txt") % (cls.category, cls.func))
        with open(os.path.join(cls.output_root, "%s-%s.txt") % (cls.category, cls.func), "w") as wf:
            wf.write(_template.render(page=cls.page, datas=dlist, factors=cls.factor_list))

    # ui automation case
    @classmethod
    def generate_automation_case(cls, dlist):
        _template = Template(
            filename=os.path.join(cls.case_template_root, "%s-%s-at.txt") % (cls.category, cls.func))
        for i in range(len(dlist)):
            with open(os.path.join(cls.output_root, "%s-%s-at-%d.py") % (cls.category, cls.func, i + 1), "w") as wf:
                wf.write(_template.render(page=cls.page, values=dlist[i], factors=cls.factor_list))
            break


class APICase(Case):
    category = "api"

    # api manual case
    @classmethod
    def generate_manual_case(cls, dlist):
        pass

    # api automation case
    @classmethod
    def generate_automation_case(cls, dlist):
        pass
