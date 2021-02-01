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
#LOG VIEW
#=============================================================


class LogView(QtWidgets.QFrame):
    def __init__(self, parent=None):
        QtWidgets.QFrame.__init__(self,parent)
        img_icon = QtGui.QImage()
        img_icon.loadFromData(Icon)
        self.setWindowIcon(QtGui.QIcon(QtGui.QPixmap.fromImage(img_icon)))
        self.setWindowTitle('Log | ' + title_project)
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
                           border: black solid 1px}
                           QGroupBox::title {
                           color: red;
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
        
        #ПО ЦЕНТРУ
        tocenter(self)
        #ГЛАВНЫЙ КОНТЕЙНЕР
        vertical_box_0 = QtWidgets.QVBoxLayout()
        group_box = QtWidgets.QGroupBox()
        vertical_box_0.addWidget(group_box)
        gorizont_box_00 = QtWidgets.QHBoxLayout()
        group_box.setLayout(gorizont_box_00)
        el_text_file = QtWidgets.QTextEdit()
        el_text_file.setFont(QtGui.QFont('Cousine',12))
        el_text_file.setLineWrapMode(QtWidgets.QTextEdit.LineWrapMode.NoWrap)
        el_text_file.setReadOnly(True)
        el_text_file.setWordWrapMode(QtGui.QTextOption.WrapMode.NoWrap)
        self.mod_doc = QtGui.QTextDocument()
        self.mod_doc.setDefaultFont(QtGui.QFont('Cousine',12))
        el_text_file.setDocument(self.mod_doc)
        gorizont_box_00.addWidget(el_text_file)
        
        #ИНДИКАТОР СТРОК
        self.ind_voprosov = QtWidgets.QLabel('Количество файлов:<b style="color:#edd220;">0</b>')
        self.ind_voprosov.setFont(QtGui.QFont('pollock2ctt',12))
        #КНОПКИ
        gorizont_box_0 = QtWidgets.QHBoxLayout()
        button_close = QtWidgets.QPushButton('Close')
        button_close.setObjectName('button_close')
        button_close.setFont(QtGui.QFont("You're Gone",15))
        img_button_close = QtGui.QImage()
        img_button_close.loadFromData(Close)
        button_close.setIcon(QtGui.QIcon(QtGui.QPixmap.fromImage(img_button_close)))
        button_close.clicked.connect(lambda:self.close())
        
        gorizont_box_0.addWidget(button_close,alignment = QtCore.Qt.AlignLeft|QtCore.Qt.AlignBottom) 
        gorizont_box_0.addWidget(self.ind_voprosov,alignment = QtCore.Qt.AlignRight|QtCore.Qt.AlignBottom)
        vertical_box_0.addLayout(gorizont_box_0)        
        self.setLayout(vertical_box_0)
        
        
            
    #ДОБАВЛЯЕМ РЕДАКТИРОВАННЫЙ ТЕКСТ
    def add_log_info(self,list):
            self.ind_voprosov.setText('Количество файлов: <b style="color:#edd220;">{}</b>'.format(len(list)))
            self.mod_doc.setHtml('<br>'.join(list))
