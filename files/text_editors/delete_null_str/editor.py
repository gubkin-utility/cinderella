#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on  05.09.2019

@author: Gubkin Leonid

Cinderella - Mass Text Editor

"""


#ФУНКЦИЯ РЕДАКТОРА
def editor(list_d):
    list_d = [i.rstrip('\r\n') for i in list_d]
    list_d = list(filter(lambda x: len(x) != 0, list_d))
    list_d = [i + '\n' for i in list_d]
    return list_d
    
    
