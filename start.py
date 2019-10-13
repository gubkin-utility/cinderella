#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on  05.09.2019

@author: Gubkin Leonid

Cinderella - Text Editor

"""

from PyQt5 import QtWidgets, QtGui, QtCore
import sys
from files.body import Body
from files.zastavka import Zastavka
import os



app =  QtWidgets.QApplication(sys.argv)

#ДОБ. ШРИФТ
QtGui.QFontDatabase.addApplicationFont(os.path.join('.','files','fonts','Xpressive-Bold.ttf'))
QtGui.QFontDatabase.addApplicationFont(os.path.join('.','files','fonts','pollock2ctt.ttf'))
QtGui.QFontDatabase.addApplicationFont(os.path.join('.','files','fonts','You-re-Gone.ttf'))
QtGui.QFontDatabase.addApplicationFont(os.path.join('.','files','fonts','Amazone-BT.ttf'))
QtGui.QFontDatabase.addApplicationFont(os.path.join('.','files','fonts','Cousine-Regular.ttf'))

FIRST = Zastavka()
WINDOW = Body()

#УДАЛЯЕМ ОБЪЕКТ ИЗ ПАМЯТИ
FIRST.setAttribute(QtCore.Qt.WA_DeleteOnClose, True)
FIRST.show()

def start_osn_window():
        FIRST.close()
        WINDOW.showMaximized()

QtCore.QTimer.singleShot(3000,start_osn_window)


sys.exit(app.exec_())