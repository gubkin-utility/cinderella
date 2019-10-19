#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on  05.09.2019

@author: Gubkin Leonid

Cinderella - Text Editor

"""

from PyQt5 import QtWidgets, QtCore
import os, shutil
import glob
from files.motor.testeditor import TestEditor
from files.text_editors.techfunction import info_size_file

class Mechanika(QtCore.QThread):
    #ДЛЯ ОСТАНОВКИ ПЕРИФЕРИЙНЫХ МОДУЛЕЙ
    stop_now = True
    value_statusbar = QtCore.pyqtSignal(int)
    mysignal = QtCore.pyqtSignal()
    def __init__(self,parent=None):
        QtCore.QThread.__init__(self,parent)
        #АТРИБУТ СТОП
        self.running = False
        #ВСЕ ФАЙЛЫ TXT
        self.allfiles = []
        #ВСЕ ФУНКЦИИ ДЛЯ РЕД. ТЕКСТА
        self.allfuncs = []
        #ВСЕГО ФАЙЛОВ
        self.vsego_files = len(self.allfiles)
        #ОСТАЛОСЬ ФАЙЛОВ
        self.ostalos_files = self.vsego_files
        #BACKUP
        self.backup = True
        #ДЛЯ ПРОСМ. ТЕСТА
        self.mytestmodule = TestEditor()
        #LOG INFO
        self.log =[]
        
    
    #BACKUP?
    def backup_yes_or_no(self,status):
        self.backup = status
        
    
    #СМОТРИМ ФАЙЛЫ В ПАПКЕ
    def files_on_folder(self,path_folder):
        self.allfiles = glob.glob(os.path.join(path_folder,'*.txt'))
        self.allfiles.sort()
        return self.allfiles

    
    #СПИСОК ФУНКЦИЙ В MECHANIKA
    def funcs_to_mechanika(self,funcs):
        self.allfuncs = funcs
        
    
    #ОТКРЫТЬ ФАЙЛ LIST
    def opentofilelist(self,file,kodirovka='utf-8'):
        with open(file,'r', encoding = kodirovka) as f:
            text = f.readlines()
        return text
    
    
    #СОХРАНИТЬ ФАЙЛ LIST
    def savetofilelist(self,path,textcontent):
        with open(path,'w', encoding='utf-8') as f:
            f.writelines(textcontent)
            
    
    #TEST ФУНКЦИЯ
    def test_edit(self):
        try:
            #СМОТРИМ РАЗМЕР ФАЙЛА
            if info_size_file(self.allfiles[0])[0] == False:
                QtWidgets.QMessageBox.critical(None,'Размер файла','Ошибка: размер файла слишком большой!' ,defaultButton = QtWidgets.QMessageBox.Ok)
            else:
                try:
                    #ОТКРЫВАЕМ ПЕРВЫЙ ФАЙЛ [LIST]
                    text_file = self.opentofilelist(self.allfiles[0])
                    #УСТАНАВЛИВАЕМ КОДИРОВКУ
                    self.mytestmodule.kodirovka = 'UTF-8'
                    
                #ЕСЛИ КОДИРОВКА НЕ UTF-8
                except:
                    from files.text_editors.techfunction import detect_encode
                    #ОПРЕДЕЛЯЕМ КОДИРОВКУ
                    code_file = detect_encode(self.allfiles[0])
                    #УСТАНАВЛИВАЕМ КОДИРОВКУ
                    self.mytestmodule.kodirovka = code_file
                    #ЕЩЕ РАЗ ОТКРЫВАЕМ ПЕРВЫЙ ФАЙЛ [LIST]
                    text_file = self.opentofilelist(self.allfiles[0],code_file)

                #ОРИГИНАЛЬНЫЙ ФАЙЛ
                orig_file = text_file.copy()
                #МАНИПУЛЯЦИИ С ФАЙЛОМ
                for f in self.allfuncs:
                    #ФУНКЦИИ КОТОРЫЕНЕ НУЖНО ОБРАБАТЫВАТЬ
                    if f.__name__ == 'split_files_edit':
                        None
                    else:
                        text_file = f(text_file)                    
                #ОРИГИНАЛ ФАЙЛ
                self.mytestmodule.add_text_edit_file(orig_file,'orig')
                #РЕДАКТ ФАЙЛ
                self.mytestmodule.add_text_edit_file(text_file,'edit')
                #ПУТЬ ФАЙЛА
                self.mytestmodule.add_text_edit_name(self.allfiles[0])
                #SHOW
                self.mytestmodule.showMaximized()
        except:
            QtWidgets.QMessageBox.critical(None,'Что то пошло не так!','Ошибка: не возможно открыть файл:\n{}\nПроверьте кодировку файла она должна быть UTF-8'.format(self.allfiles[0]) ,defaultButton = QtWidgets.QMessageBox.Ok)
            
        
        
        
    
    #ОСНОВНАЯ ФУНКЦИЯ
    def run(self):
        self.running = True
        self.log.clear()
        for i in self.allfiles:
            #ЕСЛИ РАЗМЕР ФАЙЛА СЛИШКОМ БОЛЬШОЙ ТО НЕ ОБРАБАТЫВАЕМ
            if info_size_file(i)[0] == False:
                self.log.append(i + ' - <b style="color:red;">[this file is too large][Error]</b>')
                continue
            #BACKUP
            if self.backup  == True:
                shutil.copy(i,i + '_copy')
            #ДЛЯ ОСТАНОВКИ ЦИКЛА
            if self.running == False:
                break
            try:
                #ОТКРЫВАЕМ ФАЙЛ LIST
                text_file = self.opentofilelist(i)
                #МАНИПУЛЯЦИИ С ФАЙЛОМ
                for f in self.allfuncs:
                    #ЕСЛИ НУЖНО В ФУНКЦИЮ ПЕРЕДАТЬ ПУТЬ ФАЙЛА
                    if f.__name__ == 'split_files_edit':
                        text_file = f(text_file,i)
                        #СТАТУС ЧТО СОХРАНЯТЬ В ЦИКЛЕ НЕ НАДО
                        dont_save = True
                    else:
                        text_file = f(text_file)
                        #СТАТУС ЧТО СОХРАНЯТЬ В ЦИКЛЕ НАДО
                        dont_save = False
                
                if dont_save == False:
                    #СОХРАНЯЕМ ФАЙЛ LIST
                    self.savetofilelist(i,text_file)
                self.log.append(i + ' - <b style="color:green;">[Ok]</b>')
            except UnicodeDecodeError:
                self.log.append(i + ' - <b style="color:red;">[file not utf 8 encoded][Error]</b>')
                
            except TypeError as e:
                print(e)
                self.log.append(i + ' - <b style="color:red;">[Error]</b>')
            #ЗНАЧЕНИЕ ДЛЯ СТАТУСБАРА (СКОЛЬКО ОСТАЛОСЬ)
            self.ostalos_files += 1
            self.value_statusbar.emit(self.ostalos_files)
        #УКАЗАТЕЛЬ КОНЦА ПРОЦЕССА
        self.mysignal.emit()
        
        






