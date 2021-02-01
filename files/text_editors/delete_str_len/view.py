#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on  05.09.2019

@author: Gubkin Leonid

Cinderella - Mass Text Editor

МОДУЛЬ С НАСТРОЙКАМИ
"""

from PySide2 import QtWidgets, QtGui, QtCore
from ..techfunction import title_project, tocenter, upload_options,save_options,css_style_with
from files.pics.close import Close
from files.pics.ok import Ok
from files.pics.icon import Icon



class View(QtWidgets.QFrame):
    def __init__(self,parent=None):
        QtWidgets.QFrame.__init__(self,parent)
        self.name = 'Удаление строк текста по длинне'
        self.descr = 'Модуль позволяет удалять строки текста по длинне, которые больше, равны или меньше символов'
        self.resize(300,300)
        #====================
        img_icon_project = QtGui.QImage()
        img_icon_project.loadFromData(Icon)
        self.setWindowIcon(QtGui.QIcon(QtGui.QPixmap.fromImage(img_icon_project)))
        
        self.setWindowTitle(self.name + ' | Настройки | ' + title_project)
        self.setWindowFlags(QtCore.Qt.Window|QtCore.Qt.WindowStaysOnTopHint|QtCore.Qt.MSWindowsFixedSizeDialogHint)
        self.setWindowModality(QtCore.Qt.WindowModal)
        self.setStyleSheet(css_style_with)
        tocenter(self)
        
        vertical_box_all = QtWidgets.QVBoxLayout()
        self.group_box_name = QtWidgets.QGroupBox('название модуля:')
        vertical_box_all.addWidget(self.group_box_name)
        gorizont_box = QtWidgets.QHBoxLayout()
        self.group_box_name.setLayout(gorizont_box)
        self.text_name = QtWidgets.QLineEdit()
        self.text_name.setReadOnly(True)
        self.text_name.setText(self.name)
        self.text_name.setCursorPosition(0)
        gorizont_box.addWidget(self.text_name)

        self.group_box_descr = QtWidgets.QGroupBox('описание модуля:')
        vertical_box_all.addWidget(self.group_box_descr)
        gorizont_box_descr = QtWidgets.QHBoxLayout()
        self.group_box_descr.setLayout(gorizont_box_descr)
        self.text_descr = QtWidgets.QTextEdit()
        self.text_descr.setReadOnly(True)
        self.text_descr.setLineWrapMode(QtWidgets.QTextEdit.LineWrapMode.WidgetWidth)
        self.text_descr.setText(self.descr)
        gorizont_box_descr.addWidget(self.text_descr)
        
        self.group_box_options = QtWidgets.QGroupBox('настройки модуля:')
        vertical_box_all.addWidget(self.group_box_options)
        gorizont_box_options = QtWidgets.QHBoxLayout()
        self.group_box_options.setLayout(gorizont_box_options)
        
        self.rbutton_max = QtWidgets.QRadioButton('>')
        self.rbutton_max.setToolTip('удалить все строки длиннее "N" символов')
        self.rbutton_ravno = QtWidgets.QRadioButton('=')
        self.rbutton_ravno.setToolTip('удалить все строки равные "N" символов')
        self.rbutton_min = QtWidgets.QRadioButton('<')
        self.rbutton_min.setToolTip('удалить все строки менее "N" символов')
        
        self.skolko = QtWidgets.QLineEdit()
        self.skolko.setValidator(QtGui.QIntValidator(1,1000,parent=self))
        self.skolko.setToolTip('введите необходимую длину символов от 1 до 1000')
        self.skolko.setAlignment(QtCore.Qt.AlignLeft)
        self.skolko.setCursorPosition(0)
        self.skolko.setFont(QtGui.QFont('Xpressive'))
        

        self.button_ok = QtWidgets.QPushButton()
        self.button_ok.setToolTip('сохранить настройки')
        self.button_ok.setObjectName('button_ok')
        img_button_ok = QtGui.QImage()
        img_button_ok.loadFromData(Ok)
        self.button_ok.setIcon(QtGui.QIcon(QtGui.QPixmap.fromImage(img_button_ok)))
        
        
        #ПРОБУЕМ ОТКРЫТЬ ФАЙЛ НАСТРОЕК
        all_file_options = upload_options()
        #СМОТРИМ СУЩЕСТВУЕТ ЛИ ФАЙЛ
        if len(all_file_options) > 0:
            main_options = all_file_options['delete_str_len']
            if main_options[0] == '>':
                self.rbutton_max.setChecked(True)
            elif main_options[0] == '=':
                self.rbutton_ravno.setChecked(True)
            else:
                self.rbutton_min.setChecked(True)
            #ЗАПОЛНЯЕМ ТЕКСТОВОГОЕ ПОЛЕ
            self.skolko.setText(str(main_options[1]))
        #ЕСЛИ НЕ СУЩЕСТВУЕТ
        else:
            self.rbutton_up.setChecked(True)
            QtWidgets.QMessageBox.critical(self,'Файл настроек не найден или поврежден','Внимание файл настроек settings.json не найден или поврежден. Дальнейшая работа программы не возможна!', defaultButton = QtWidgets.QMessageBox.Ok)
            
        #СОХРАНЯЕМ НАСТРОЙКИ
        def button_save_options():
            now_option = []
            try:
                if self.rbutton_max.isChecked() == True:
                    summ = '>'
                elif self.rbutton_ravno.isChecked() == True:
                    summ = '='   
                else:
                    summ = '<'
                    
                now_option.append(summ)
                if len(self.skolko.text()) == 0:
                    dlinna = 0
                else:
                    dlinna = int(self.skolko.text())
                now_option.append(dlinna)
                
                all_file_options['delete_str_len'] = now_option

                save_options(all_file_options)
                self.button_ok.setStyleSheet('background-color: green;')
            except:
                QtWidgets.QMessageBox.critical(self,'Настройки не сохранены!','Возможно файл настроек settings.json не найден или поврежден. Дальнейшая работа программы не возможна!', defaultButton = QtWidgets.QMessageBox.Ok)

        
        self.button_ok.clicked.connect(button_save_options)
        self.rbutton_max.toggled.connect(lambda:self.button_ok.setStyleSheet('background-color: #e9e9e9;'))
        self.rbutton_ravno.toggled.connect(lambda:self.button_ok.setStyleSheet('background-color: #e9e9e9;'))
        self.rbutton_min.toggled.connect(lambda:self.button_ok.setStyleSheet('background-color: #e9e9e9;'))
        gorizont_box_options.addWidget(self.rbutton_max,alignment = QtCore.Qt.AlignCenter)
        gorizont_box_options.addWidget(self.rbutton_ravno,alignment = QtCore.Qt.AlignCenter)
        gorizont_box_options.addWidget(self.rbutton_min,alignment = QtCore.Qt.AlignCenter)
        gorizont_box_options.addWidget(self.skolko,alignment = QtCore.Qt.AlignCenter)
        gorizont_box_options.addWidget(self.button_ok,alignment = QtCore.Qt.AlignCenter)

        button_close = QtWidgets.QPushButton('Close')
        button_close.setFont(QtGui.QFont("You're Gone",15))
        button_close.setObjectName('button_close')
        img_button_close = QtGui.QImage()
        img_button_close.loadFromData(Close)
        button_close.setIcon(QtGui.QIcon(QtGui.QPixmap.fromImage(img_button_close)))
        button_close.clicked.connect(lambda:self.close())
        
        vertical_box_all.addWidget(button_close,alignment = QtCore.Qt.AlignHCenter)
        self.setLayout(vertical_box_all)
        self.show()
        
