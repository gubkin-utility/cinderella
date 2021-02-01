#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on  05.09.2019

@author: Gubkin Leonid

Cinderella - Mass Text Editor

"""

from PySide2 import QtWidgets, QtGui, QtCore
from files.text_editors.techfunction import title_project,tocenter
from files.pics.close import Close
from files.pics.icon import Icon

#=============================================================
#TEST EDITOR
#=============================================================



class TestEditor(QtWidgets.QFrame):
    def __init__(self, parent=None):
        QtWidgets.QFrame.__init__(self,parent)
        img_icon = QtGui.QImage()
        img_icon.loadFromData(Icon)
        self.setWindowIcon(QtGui.QIcon(QtGui.QPixmap.fromImage(img_icon)))
        self.setWindowTitle('Test | ' + title_project)
        self.setWindowFlags(QtCore.Qt.Window|QtCore.Qt.WindowStaysOnTopHint|QtCore.Qt.MSWindowsFixedSizeDialogHint)
        self.setWindowModality(QtCore.Qt.WindowModal)
        self.setStyleSheet("""
                           QWidget{ 
                           background-color: #24313c;
                           color : #8e949a;
                           }
                           QToolTip { 
                           background-color: yellow; 
                           color: black; 
                           border: black solid 1px
                           }
                           QGroupBox{
                           color: red;
                           subcontrol-position: top left;
                           font-size: 21px;
                           font-family: Xpressive;
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
                           """)
        self.setMinimumSize(800,600)
        self.skolko_strok = 0
        self.skolko_strok_edit = 0
        self.kodirovka = '-'
        #ПО ЦЕНТРУ
        tocenter(self)
        #ГЛАВНЫЙ КОНТЕЙНЕР
        vertical_box_0 = QtWidgets.QVBoxLayout()
        group_box = QtWidgets.QGroupBox()
        vertical_box_0.addWidget(group_box, alignment = QtCore.Qt.AlignTop)
        gorizont_box_00 = QtWidgets.QHBoxLayout()
        group_box.setLayout(gorizont_box_00)
        label_name_file = QtWidgets.QLabel('Path to file: ')
        label_name_file.setFont(QtGui.QFont('Xpressive',13))
        self.el_name_file = QtWidgets.QLineEdit()
        self.el_name_file.setReadOnly(True)
        self.el_name_file.setAlignment(QtCore.Qt.AlignLeft)
        self.el_name_file.setCursorPosition(0)
        self.el_name_file.setFont(QtGui.QFont('Xpressive',12))
        gorizont_box_00.addWidget(label_name_file)
        gorizont_box_00.addWidget(self.el_name_file)
        
        gorizont_box_01 = QtWidgets.QHBoxLayout()
        vertical_box_0.addLayout(gorizont_box_01)
        self.group_box_orig = QtWidgets.QGroupBox('After: ')
        self.group_box_orig.setToolTip('Файл до редактирования')
        group_box_edit = QtWidgets.QGroupBox('Before:')
        group_box_edit.setToolTip('Файл после редактирование')
        gorizont_box_01.addWidget(self.group_box_orig)
        gorizont_box_01.addWidget(group_box_edit)
        vertical_box_orig = QtWidgets.QVBoxLayout()
        vertical_box_edit = QtWidgets.QVBoxLayout()
        self.group_box_orig.setLayout(vertical_box_orig)
        group_box_edit.setLayout(vertical_box_edit)
        #ДО ТЕКСТ
        self.el_text_file = QtWidgets.QTextEdit()
        self.el_text_file.setLineWrapMode(QtWidgets.QTextEdit.LineWrapMode.NoWrap)
        self.el_text_file.setReadOnly(True)
        self.el_text_file.setWordWrapMode(QtGui.QTextOption.WrapMode.NoWrap)
        self.mod_doc = QtGui.QTextDocument()
        self.mod_doc.setDefaultFont(QtGui.QFont('Cousine',12))
        self.el_text_file.setDocument(self.mod_doc)
        self.el_text_file.moveCursor(QtGui.QTextCursor.Start)
        vertical_box_orig.addSpacing(15)
        vertical_box_orig.addWidget(self.el_text_file)
        ind_voprosov_orig = QtWidgets.QLabel('Количество строк: <b style="color:#edd220;">{}</b>'.format(0))
        gorizont_box_07 = QtWidgets.QHBoxLayout()
        ind_voprosov_orig.setFont(QtGui.QFont('pollock2ctt',12))
        gorizont_box_07.addWidget(ind_voprosov_orig,alignment = QtCore.Qt.AlignRight|QtCore.Qt.AlignBottom)
        gorizont_box_07.addStretch(500)
        
        ind_coding_orig = QtWidgets.QLabel('Кодировка файла: <b style="color:#edd220;">{}</b>'.format(self.kodirovka))
        ind_coding_orig.setFont(QtGui.QFont('pollock2ctt',12))
        gorizont_box_07.addWidget(ind_coding_orig,alignment = QtCore.Qt.AlignLeft|QtCore.Qt.AlignBottom)
        vertical_box_orig.addLayout(gorizont_box_07)
        
        
        #ИНДИКАТОР КОДИРОВКИ 
        def changed_cod_orig():
            ind_coding_orig.setText('Кодировка файла: <b style="color:#edd220;">{}</b>'.format(self.kodirovka))
            
            
        #ПОСЛЕ ТЕКСТ
        self.el_text_file_edit = QtWidgets.QTextEdit()
        self.el_text_file_edit.setLineWrapMode(QtWidgets.QTextEdit.LineWrapMode.NoWrap)
        self.el_text_file_edit.setReadOnly(True)
        self.el_text_file_edit.setWordWrapMode(QtGui.QTextOption.WrapMode.NoWrap)
        self.mod_doc_edit = QtGui.QTextDocument()
        self.mod_doc_edit.setDefaultFont(QtGui.QFont('Cousine',12))
        self.el_text_file_edit.setDocument(self.mod_doc_edit)
        vertical_box_edit.addSpacing(15)
        vertical_box_edit.addWidget(self.el_text_file_edit)
        ind_voprosov_edit = QtWidgets.QLabel('Количество строк: <b style="color:#edd220;">{}</b>'.format(0))
        ind_voprosov_edit.setFont(QtGui.QFont('pollock2ctt',12))
        vertical_box_edit.addWidget(ind_voprosov_edit,alignment = QtCore.Qt.AlignRight|QtCore.Qt.AlignBottom)

        
        #ИНДИКАТОР СТРОК 
        def changed_str_orig():
            ind_voprosov_orig.setText('Количество строк: <b style="color:#edd220;">{}</b>'.format(self.skolko_strok))
            
        def changed_str_edit():
            ind_voprosov_edit.setText('Количество строк: <b style="color:#edd220;">{}</b>'.format(self.skolko_strok_edit))
      
        self.mod_doc.contentsChanged.connect(changed_str_orig)
        self.mod_doc_edit.contentsChanged.connect(changed_str_edit)

        self.mod_doc.contentsChanged.connect(changed_cod_orig)
        
        
        #КНОПКИ
        gorizont_box_0 = QtWidgets.QHBoxLayout()
        button_close = QtWidgets.QPushButton('Close')
        button_close.setObjectName('button_close')
        button_close.setFont(QtGui.QFont("You're Gone",15))
        
        img_button_close = QtGui.QImage()
        img_button_close.loadFromData(Close)
        button_close.setIcon(QtGui.QIcon(QtGui.QPixmap.fromImage(img_button_close)))
        button_close.clicked.connect(lambda:self.close())
        #ИНДИКАТОР ДЛЯ ПРЕДУПРЕЖДЕНИЙ
        self.ind = QtWidgets.QLabel() 
        self.ind.setFont(QtGui.QFont('pollock2ctt',12))
        gorizont_box_0.addWidget(button_close,alignment = QtCore.Qt.AlignLeft|QtCore.Qt.AlignBottom)
        gorizont_box_0.addWidget(self.ind,alignment = QtCore.Qt.AlignLeft|QtCore.Qt.AlignBottom)
        vertical_box_0.addLayout(gorizont_box_0)
        
        self.group_box_orig.setSizePolicy(QtWidgets.QSizePolicy.Minimum,QtWidgets.QSizePolicy.Minimum)
        group_box_edit.setSizePolicy(QtWidgets.QSizePolicy.Minimum,QtWidgets.QSizePolicy.Minimum)
        
        self.setLayout(vertical_box_0)
        
        
    
        
    #ДОБАВЛЯЕМ РЕДАКТИРОВАННЫЙ ТЕКСТ
    def add_text_edit_file(self,list,st):
        #ЕСЛИ ФАЙЛ СЛИШКОМ ДЛИННЫЙ ТО ОБРЕЗАЕМ ЕГО
        if len(list) > 5000:
            list = list[:5000]
            self.ind.setText('<span style="color:red;">Внимание: Файл обрезан до 5000 строк</span>')

        #ДОБАВЛ. К ТЕКСТУ НОМЕРА СТРОК
        def add_n_lines(list):
            #ДЛИННА СПИСКА
            dlinna = len(str(len(list)))
            #НАЧАЛЬНОЕ ЗНАЧЕНИЕ СТРОКИ
            n = 1
            #ЦИКЛ ДОЮАВЛЕНИЯ
            for i in list.copy():
                #СКОЛЬКО ПРОБЕЛЛОВ ДОБАВИТЬ
                dd = (dlinna - len(str(n)))
                #СБОРКА СТРОКИ
                list[list.index(i)] = '<span style="color:yellow;background-color: #9854ff;">' + '&nbsp;'*dd + str(n) + '.' + '</span>' + ' ' + i
                n+=1 
            return list
        
        add_n_lines(list)
        #ПРЕОБРАЗУЕМ LIST -> STR
        if st == 'orig':
            self.skolko_strok = len(list)
            self.mod_doc.setHtml('<br>'.join(list))
            #КУРСОР НА ВЕРХ
            self.el_text_file.moveCursor(QtGui.QTextCursor.Start)
        else:
            self.skolko_strok_edit = len(list)
            self.mod_doc_edit.setHtml('<br>'.join(list))
            #КУРСОР НА ВЕРХ
            self.el_text_file_edit.moveCursor(QtGui.QTextCursor.Start)
 
    
    
    #ДОБАВЛЯЕМ ИМЯ ФАЙЛА
    def add_text_edit_name(self,str):
        self.el_name_file.setText(str)