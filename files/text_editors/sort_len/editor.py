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
    main_options = upload_options()['sort_len_view']
    
    if main_options == 'rbutton_up':
        list.sort(key= len)
    else:
        list.sort(key= len,reverse = True)
    return list
        
