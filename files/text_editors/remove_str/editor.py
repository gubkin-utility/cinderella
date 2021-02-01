#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on  05.09.2019

@author: Gubkin Leonid

Cinderella - Mass Text Editor

"""

from ..techfunction import upload_options



#ФУНКЦИЯ РЕДАКТОРА
def editor(list):
    #ПРОБУЕМ ОТКРЫТЬ ФАЙЛ НАСТРОЕК
    main_options = upload_options()['remove_str']
    
    def standart(i):
        return i.replace(main_options[0],main_options[1])
    
    list = [standart(i) for i in list]

    return list