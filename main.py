#!/usr/bin/env python
# coding=utf8

"""
-------------------------------------------------
   File Name:     main
   Description:
   Author:        anderson
   date:          2019-11-25
-------------------------------------------------
"""

__version__ = "1.0.0"

from user.case import CASE_MAP
import sys


if __name__ == "__main__":
    # user run case by command line like (python3 ./main.py login,navigation ui)
    params = sys.argv
    func_list = [parm.strip() for parm in params[1].split(",")]
    if len(params) < 3:
        category = "ui"
    else:
        category = params[2]

    [CASE_MAP[category][func].run() for func in func_list]
