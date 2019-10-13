#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on  05.09.2019

@author: Gubkin Leonid

Cinderella - Text Editor

"""

from PyQt5 import QtWidgets, QtGui, QtCore
from files.text_editors.techfunction import title_project,icon_project,tocenter
import sys, os
#=============================================================
#LOG VIEW
#=============================================================


class LogView(QtWidgets.QWidget):
    def __init__(self, parent=None):
        QtWidgets.QFrame.__init__(self,parent)
        self.setWindowIcon(QtGui.QIcon(icon_project))
        self.setWindowTitle('Log | ' + title_project)
        self.setStyleSheet('background-color: #e9e9e9; color : black;')
        self.setStyleSheet("""
                           QToolTip { 
                           background-color: yellow; 
                           color: black; 
                           border: black solid 1px}
                           QWidget{ 
                           background-color: #bae1ff;
                           color : black;}
                           QGroupBox::title {
                           color: red;
                           font-family: Xpressive;}
                           """)
        self.resize(800,600)
        #ПО ЦЕНТРУ
        tocenter(self)
        #ГЛАВНЫЙ КОНТЕЙНЕР
        vertical_box_0 = QtWidgets.QVBoxLayout()
        group_box = QtWidgets.QGroupBox()
        vertical_box_0.addWidget(group_box)
        gorizont_box_00 = QtWidgets.QHBoxLayout()
        group_box.setLayout(gorizont_box_00)
        el_text_file = QtWidgets.QTextEdit()
        el_text_file.setFont(QtGui.QFont('Cousine'))
        el_text_file.setLineWrapMode(0)
        el_text_file.setReadOnly(True)
        el_text_file.setWordWrapMode(0)
        self.mod_doc = QtGui.QTextDocument()
        el_text_file.setDocument(self.mod_doc)
        gorizont_box_00.addWidget(el_text_file)
        
        #ИНДИКАТОР СТРОК
        self.ind_voprosov = QtWidgets.QLabel('Количество файлов:<b style="color:navy;">0</b>')
        self.ind_voprosov.setFont(QtGui.QFont('pollock2ctt'))
        #КНОПКИ
        gorizont_box_0 = QtWidgets.QHBoxLayout()
        button_close = QtWidgets.QPushButton('Close')
        button_close.setFont(QtGui.QFont("You're Gone"))
        button_close.setStyleSheet('background-color: #fcaecd')
        button_close.setIcon(QtGui.QIcon(os.path.join('.','files','pic','close.png')))
        button_close.clicked.connect(lambda:self.close())
        
        gorizont_box_0.addWidget(button_close,alignment = QtCore.Qt.AlignLeft|QtCore.Qt.AlignBottom) 
        gorizont_box_0.addWidget(self.ind_voprosov,alignment = QtCore.Qt.AlignRight|QtCore.Qt.AlignBottom)
        vertical_box_0.addLayout(gorizont_box_0)        
        self.setLayout(vertical_box_0)
        
        
            
    #ДОБАВЛЯЕМ РЕДАКТИРОВАННЫЙ ТЕКСТ
    def add_log_info(self,list):
            self.ind_voprosov.setText('Количество файлов:<b style="color:navy;">{}</b>'.format(len(list)))
            self.mod_doc.setHtml('<br>'.join(list))
