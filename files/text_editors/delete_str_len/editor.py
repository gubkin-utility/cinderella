#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on  05.09.2019

@author: Gubkin Leonid

Cinderella - Mass Text Editor

"""

from ..techfunction import upload_options



#ФУНКЦИЯ РЕДАКТОРА
def editor(list1):
    #ПРОБУЕМ ОТКРЫТЬ ФАЙЛ НАСТРОЕК
    #main_options[0]- >=<,main_options[1]- ДЛИННА 
    main_options = upload_options()['delete_str_len']
    list1 = [i.rstrip('\r\n') for i in list1]
    if main_options[0] == '>':
        result = filter(lambda x: not len(x) > main_options[1], list1)
    elif main_options[0] == '=':
        result = filter(lambda x: len(x) != main_options[1], list1)
    else:
        result = filter(lambda x: not len(x) < main_options[1], list1)
    return list([i + '\n' for i in result])
        
