#!/usr/bin/env python
# coding=utf8

"""
-------------------------------------------------
   File Name:     config
   Description:
   Author:        anderson
   date:          2019-11-25
-------------------------------------------------
"""

from core.common.parseutil import ConfigParser
from core.case.policy import Policy
import subprocess
import os


class Config(object):

    @classmethod
    def generate_pict_input_file(cls, pict_input_file):
        user_config_lines = list()
        with open(pict_input_file, "w") as wf:
            for item in ConfigParser.get_section('includeChars'):
                # generate basic conf combine based on rule [null, full, part] which need manual intervention.
                user_config_lines.append("%s: " % item)
                Policy.apply_policies(user_config_lines,
                                      [char.strip() for char in ConfigParser.get_option('includeChars', item).split(",")],
                                      int(ConfigParser.get_option('minLength', item)))
            wf.writelines(user_config_lines)

    @classmethod
    def generate_pict_output_list(cls, pict_input_file):
        # pict process then output result file
        p = subprocess.Popen(os.path.join(os.getcwd(), "core/common/pict %s" % pict_input_file), shell=True,
                             stdout=subprocess.PIPE, universal_newlines=True)
        p.wait()
        os.remove(pict_input_file)
        return p.stdout.readlines()

    @classmethod
    def get_pict_output_factor_list(cls, pict_output_list):
        return [factor.strip() for factor in pict_output_list[0].split("\t")]

    @classmethod
    def get_pict_output_data_list(cls, pict_output_list):
        return [line.strip().split("\t") for line in pict_output_list[1:]]
