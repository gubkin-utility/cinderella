#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on  05.09.2019

@author: Gubkin Leonid

Cinderella - Text Editor

"""

from collections import OrderedDict


#ФУНКЦИЯ РЕДАКТОРА
def editor(list1):
    list1 = list(OrderedDict.fromkeys(list1))
    return list1
