#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on  05.09.2019

@author: Gubkin Leonid

Cinderella - Mass Text Editor

"""

from ..techfunction import upload_options,savetofilelist
import datetime
import os
from ...motor.mechanika import Mechanika


#ДЛЯ ГЕНЕРАЦИИ УНИКАЛЬНОГО ЗАГОЛОВКА
def generate_file_name(name):
    uniq_filename = str(datetime.datetime.now().time()).replace(':', '-').replace('.','-')
    return name.rstrip('.txt') + '_' + uniq_filename + '.txt'
    

#ФУНКЦИЯ РЕДАКТОРА
def editor(list,i,kodirovka):
    #ПРОБУЕМ ОТКРЫТЬ ФАЙЛ НАСТРОЕК
    skolko = int(upload_options()['split_files'])
    path = os.path.dirname(i)
    name = os.path.basename(i)
    while len(list) > 0:
        if Mechanika.stop_now == False:
            break
        sres = list[:skolko]
        path_for_file = os.path.join(path,generate_file_name(name))
        savetofilelist(path_for_file,sres,kodirovka)
        for i in range(len(sres)):
            list.remove(sres.pop(0))