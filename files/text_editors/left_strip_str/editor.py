#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on  05.09.2019

@author: Gubkin Leonid

Cinderella - Mass Text Editor

"""


#ФУНКЦИЯ РЕДАКТОРА
def editor(list_d):
    def tech(str1):
        str1 = str1.lstrip()
        if len(str1) == 0:
            str1 = str1 + '\n'
        return str1
    
    list_d = [tech(i) for i in list_d]
    
    return list_d
    
    
