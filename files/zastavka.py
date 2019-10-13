#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on  05.09.2019

@author: Gubkin Leonid

Cinderella - Text Editor

"""


from PyQt5 import QtWidgets, QtGui, QtCore
from files.text_editors.techfunction import tocenter,title_project,icon_project
import os

#=============================================================
#ЗАСТАВКА
#=============================================================

class Zastavka(QtWidgets.QWidget):
    def __init__(self,parent=None):
        QtWidgets.QWidget.__init__(self,parent)
        self.setWindowIcon(QtGui.QIcon(icon_project))
        self.setWindowTitle(title_project)
        self.setWindowFlags(QtCore.Qt.Window|QtCore.Qt.FramelessWindowHint)
        #ПО ЦЕНТРУ
        tocenter(self)
        pixmap = QtGui.QPixmap(os.path.join('.','files','pic','zastavka.png'))
        pal = self.palette()
        pal.setBrush(QtGui.QPalette.Normal,QtGui.QPalette.Window,QtGui.QBrush(pixmap))
        pal.setBrush(QtGui.QPalette.Inactive,QtGui.QPalette.Window,QtGui.QBrush(pixmap))
        self.setPalette(pal)
        self.setMask(pixmap.mask())
        
        
        
        

   
