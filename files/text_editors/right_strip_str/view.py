#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on  05.09.2019

@author: Gubkin Leonid

Cinderella - Mass Text Editor

МОДУЛЬ БЕЗ НАСТРОЕК
"""

from PySide2 import QtWidgets, QtGui, QtCore
from ..techfunction import title_project, tocenter,css_style_without
from files.pics.close import Close
from files.pics.icon import Icon


class View(QtWidgets.QFrame):
    def __init__(self,parent=None):
        QtWidgets.QFrame.__init__(self,parent)
        self.name = 'Удаление пустот в конце строки'
        self.descr = 'Модуль позволяет удалить пустоты в конце строки(\\t,\\s) в файле(ах)'
        self.resize(300,300)
        #====================
        img_icon = QtGui.QImage()
        img_icon.loadFromData(Icon)
        self.setWindowIcon(QtGui.QIcon(QtGui.QPixmap.fromImage(img_icon)))
        self.setWindowTitle(self.name + ' | Настройки | ' + title_project)
        self.setWindowFlags(QtCore.Qt.Window|QtCore.Qt.WindowStaysOnTopHint|QtCore.Qt.MSWindowsFixedSizeDialogHint)
        self.setWindowModality(QtCore.Qt.WindowModal)
        self.setStyleSheet(css_style_without)
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
        text_descr = QtWidgets.QTextEdit()
        text_descr.setReadOnly(True)
        text_descr.setLineWrapMode(QtWidgets.QTextEdit.LineWrapMode.WidgetWidth)
        text_descr.setText(self.descr)
        gorizont_box_descr.addWidget(text_descr)
        
        self.group_box_options = QtWidgets.QGroupBox('настройки модуля:')
        vertical_box_all.addWidget(self.group_box_options)
        gorizont_box_options = QtWidgets.QHBoxLayout()
        self.group_box_options.setLayout(gorizont_box_options)
        self.text_options = QtWidgets.QTextEdit()
        self.text_options.setReadOnly(True)
        self.text_options.setLineWrapMode(QtWidgets.QTextEdit.LineWrapMode.WidgetWidth)
        self.text_options.setText('Модуль не имеет настроек')
        gorizont_box_options.addWidget(self.text_options)
        
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
    
    
    
   



