#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on  05.09.2019

@author: Gubkin Leonid

Cinderella - Mass Text Editor

"""


from PySide2 import QtWidgets
import os
import json
import glob
from psutil import virtual_memory


title_project = 'Cinderella'


#СТИЛИ ДЛЯ МОДУЛЕЙ БЕЗ НАСТРОЕК
css_style_without = '''
                        QWidget{ 
                        background-color: #24313c;
                        color : #8e949a;
                        }  
                        QToolTip { 
                        background-color: yellow; 
                        color: black; 
                        border: black solid 1px
                        }
                        QLineEdit{
                        background-color: #d7fde6;
                        color : black;
                        font-family: Cousine;
                        font-size: 12px;
                        }
                        QTextEdit{
                        background-color: #d7fde6;
                        color : black;
                        font-family: Cousine;
                        font-size: 12px;
                        margin-top: 15px;
                        }
                        QGroupBox{
                        color: #edd220;
                        font-family: Xpressive;
                        font-size: 12px;
                        }
                        QPushButton#button_close:enabled {
                        background-color: #fed3f6;
                        border: 1px inset #000000;
                        border-radius: 5px;
                        color: #101b15;
                        padding: 5px;
                        width: 80px;
                        }
                        QPushButton#button_close:hover {
                        background-color: #fea9f6;
                        border: 1px inset #000000;
                        border-radius: 5px;
                        color: #101b15;
                        padding: 5px;
                        width: 80px;
                        }   
                        QPushButton#button_close:pressed{
                        background-color: #fea9bb;
                        border: 1px inset #000000;
                        border-radius: 5px;
                        color: #101b15;
                        padding: 5px;
                        width: 80px;
                        }
                        QPushButton#button_close:disabled {
                        background-color: #dadfe4;
                        border: 1px inset #000000;
                        border-radius: 5px;
                        color: #101b15;
                        padding: 5px;
                        width: 80px;
                        }
                            
                        '''

#СТИЛИ ДЛЯ МОДУЛЕЙ С НАСТРОЙКАМИ
css_style_with = '''
                    QWidget{ 
                    background-color: #24313c;
                    color : #8e949a;
                    }  
                    QToolTip { 
                    background-color: yellow; 
                    color: black; 
                    border: black solid 1px
                    }
                    QLineEdit{
                    background-color: #e5e5e5;
                    color : black;
                    font-family: Cousine;
                    font-size: 12px;
                    margin-top: 15px;
                    }
                    QTextEdit{
                    background-color: #e5e5e5;
                    color : black;
                    font-family: Cousine;
                    font-size: 12px;
                    margin-top: 15px;
                    }
                    QGroupBox{
                    color: #edd220;
                    font-family: Xpressive;
                    font-size: 12px;
                    }
                    QPushButton#button_close:enabled {
                    background-color: #fed3f6;
                    border: 1px inset #000000;
                    border-radius: 5px;
                    color: #101b15;
                    padding: 5px;
                    width: 80px;
                    }
                    QPushButton#button_close:hover {
                    background-color: #fea9f6;
                    border: 1px inset #000000;
                    border-radius: 5px;
                    color: #101b15;
                    padding: 5px;
                    width: 80px;
                    }   
                    QPushButton#button_close:pressed{
                    background-color: #fea9bb;
                    border: 1px inset #000000;
                    border-radius: 5px;
                    color: #101b15;
                    padding: 5px;
                    width: 80px;
                    }
                    QPushButton#button_ok:enabled {
                    background-color: #e9e9e9;
                    border: 1px inset #000000;
                    border-radius: 5px;
                    color: #101b15;
                    padding: 1px;
                    width: 25px;
                    height: 25px;
                    }
                    QPushButton#button_ok:hover {
                    background-color: #c7e9e9;
                    border: 1px inset #000000;
                    border-radius: 5px;
                    color: #101b15;
                    padding: 1px;
                    width: 25px;
                    height: 25px;
                    }   
                    QPushButton#button_ok:pressed{
                    background-color: #90e9ac;
                    border: 1px inset #000000;
                    border-radius: 5px;
                    color: #101b15;
                    padding: 1px;
                    width: 25px;
                    height: 25px;
                    }

                    '''


#СОХРАНЕНИЕ В ФАЙЛ LIST
def savetofilelist(file,text,kodirovka='utf-8'):
    with open(file,'w', encoding=kodirovka) as f:
        f.writelines(text)
        

#ДОБАВЛЕНИЕ В ФАЙЛ LIST
def addtofilelist(file,text,kodirovka='utf-8'):
    with open(file,'a', encoding=kodirovka) as f:
        f.writelines(text)

        
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
    x = (desktop.width() - nowelement.size().width()) // 2
    y = (desktop.height() - nowelement.size().height()) // 2
    nowelement.move(x,y)



#СМОТРИМ ФАЙЛЫ В ПАПКЕ
def files_on_folder(path_folder):
    allfiles = glob.glob(os.path.join(path_folder,'*.txt'))
    return allfiles

