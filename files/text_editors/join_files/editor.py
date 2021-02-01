#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on  05.09.2019

@author: Gubkin Leonid

Cinderella - Mass Text Editor

"""

from ..techfunction import addtofilelist
import os
    

#ФУНКЦИЯ РЕДАКТОРА
def editor(list,i,kodirovka):
    path = os.path.dirname(i)
    ok_path = os.path.join(path,'OUTPUT.txt')
    addtofilelist(ok_path,list,kodirovka)