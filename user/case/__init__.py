#!/usr/bin/env python
# coding=utf8

"""
-------------------------------------------------
   File Name:     __init__.py
   Description:
   Author:        anderson
   date:          2019-11-26
-------------------------------------------------
"""

from core.case.case import UICase


# login page ui case
class LoginUICase(UICase):
    page = "login"
    func = "login"


CASE_MAP = {
    "ui": {
        "login": LoginUICase
    }
}
