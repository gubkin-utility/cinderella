#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on  05.09.2019

@author: Gubkin Leonid

Cinderella - Mass Text Editor

"""

from PySide2 import QtWidgets, QtGui, QtCore
from files.text_editors.techfunction import tocenter,title_project
from files.pics.cinderella_zastavka import Cinderella_Zastavka
from files.pics.icon import Icon



#=============================================================
#ЗАСТАВКА
#=============================================================

class Zastavka(QtWidgets.QWidget):
    def __init__(self,parent=None):
        QtWidgets.QWidget.__init__(self,parent)
        img_icon = QtGui.QImage()
        img_icon.loadFromData(Icon)
        self.setWindowIcon(QtGui.QIcon(QtGui.QPixmap.fromImage(img_icon)))
        self.setWindowTitle(title_project)
        self.setWindowFlags(QtCore.Qt.Window|QtCore.Qt.FramelessWindowHint)
        img_header_l = QtGui.QImage()
        img_header_l.loadFromData(Cinderella_Zastavka)        
        pixmap = QtGui.QPixmap.fromImage(img_header_l)
        pal = self.palette()
        pal.setBrush(QtGui.QPalette.Normal,QtGui.QPalette.Window,QtGui.QBrush(pixmap))
        pal.setBrush(QtGui.QPalette.Inactive,QtGui.QPalette.Window,QtGui.QBrush(pixmap))
        self.setPalette(pal)
        self.setMask(pixmap.mask())
        #ПО ЦЕНТРУ
        self.resize(430,294)
        tocenter(self)
        
        
        

   
