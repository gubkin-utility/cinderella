#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on  05.09.2019

@author: Gubkin Leonid

Cinderella - Text Editor

"""


from PyQt5 import QtWidgets
import os
import json
import glob
from psutil import virtual_memory


title_project = 'Cinderella'
icon_project = os.path.join('.','files','pic','icon.png')




#КОДИРОВКА ФАЙЛА
def detect_encode(file):
    from chardet.universaldetector import UniversalDetector
    detector = UniversalDetector()
    detector.reset()
    with open(file, 'rb') as f:
        for row in f:
            detector.feed(row)
            if detector.done: break
    detector.close()
    return detector.result.get('encoding')


#СМОТРИМ РАЗМЕР ФАЙЛА
def info_size_file(file_path):
    file_size = int(os.path.getsize(file_path))
    sys_size = int(virtual_memory().available)
    if sys_size > file_size:
        status = True
    else:
        status = False
    return status,file_size,sys_size


#ЗАГРУЖАЕМ НАСТРОЙКИ
def upload_options():
    try:
        with open("settings.json", "r") as read_file:
            data_options = json.load(read_file)
    except:
        data_options = {}
    return data_options


#СОХРАНЯЕМ НАСТРОЙКИ
def save_options(data):
    with open("settings.json", "w") as write_file:
        json.dump(data, write_file)

    
#ОКНО ПО ЦЕНТРУ
def tocenter(nowelement):
    nowelement.move(nowelement.width() * -2,0)
    desktop = QtWidgets.QApplication.desktop()
    x = (desktop.width() - nowelement.frameSize().width()) // 2
    y = (desktop.height() - nowelement.frameSize().height()) // 2
    nowelement.move(x,y)




#СМОТРИМ ФАЙЛЫ В ПАПКЕ
def files_on_folder(path_folder):
    allfiles = glob.glob(os.path.join(path_folder,'*.txt'))
    return allfiles

