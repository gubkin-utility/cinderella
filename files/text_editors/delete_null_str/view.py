#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on  05.09.2019

@author: Gubkin Leonid

Cinderella - Text Editor

МОДУЛЬ БЕЗ НАСТРОЕК
"""

from PyQt5 import QtWidgets, QtGui, QtCore
import os
from ..techfunction import title_project,icon_project, tocenter


class View(QtWidgets.QWidget):
    def __init__(self,parent=None):
        QtWidgets.QFrame.__init__(self,parent)
        self.name = 'Удаление пустых строк'
        self.descr = 'Модуль позволяет удалить пустые строки(строки содержащие только специальные символы \\r,\\n,\\t,\\s,\\b) в файле(ах)'
        self.resize(300,300)
        #====================
        self.setWindowIcon(QtGui.QIcon(icon_project))
        self.setWindowTitle(self.name + ' | Настройки | ' + title_project)
        self.setWindowFlags(QtCore.Qt.Window|QtCore.Qt.WindowStaysOnTopHint|QtCore.Qt.MSWindowsFixedSizeDialogHint)
        self.setWindowModality(QtCore.Qt.WindowModal)
        self.setStyleSheet("""
                           QToolTip { 
                           background-color: yellow; 
                           color: black; 
                           border: black solid 1px}
                           QWidget{ 
                           background-color: #1def6f;
                           color : black;}
                           QLineEdit{
                           background-color: yellow;
                           color : black;
                           font-family: Cousine;}
                           QTextEdit{
                           background-color: yellow;
                           color : black;
                           font-family: Cousine;}
                           QGroupBox{
                           color: navy;
                           font-family: Xpressive;}
                            """)
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
        text_descr.setLineWrapMode(1)
        text_descr.setText(self.descr)
        gorizont_box_descr.addWidget(text_descr)
        
        self.group_box_options = QtWidgets.QGroupBox('настройки модуля:')
        vertical_box_all.addWidget(self.group_box_options)
        gorizont_box_options = QtWidgets.QHBoxLayout()
        self.group_box_options.setLayout(gorizont_box_options)
        self.text_options = QtWidgets.QTextEdit()
        self.text_options.setReadOnly(True)
        self.text_options.setLineWrapMode(1)
        self.text_options.setText('Модуль не имеет настроек')
        gorizont_box_options.addWidget(self.text_options)
        
        button_close = QtWidgets.QPushButton('Close')
        button_close.setFont(QtGui.QFont("You're Gone"))
        button_close.setStyleSheet('background-color: #fcaecd')
        button_close.setIcon(QtGui.QIcon(os.path.join('.','files','pic','close.png')))
        button_close.clicked.connect(lambda:self.close())
        
        vertical_box_all.addWidget(button_close,alignment = QtCore.Qt.AlignHCenter)
        self.setLayout(vertical_box_all)
        self.show()
    
    
    
   



