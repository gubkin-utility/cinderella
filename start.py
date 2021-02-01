#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on  05.09.2019

@author: Gubkin Leonid

Cinderella - Mass Text Editor

"""

from PySide2 import QtWidgets, QtGui, QtCore
import sys
from files.body import Body
from files.zastavka import Zastavka
from files.fonts.cousineregular import CousineRegular
from files.fonts.xpressivebold import XpressiveBold
from files.fonts.amazonebt import AmazoneBt
from files.fonts.youregone import YouReGone
from files.fonts.pollock2ctt import Pollock2ctt



#FOR ERROR
error_to_file = open(r'error.txt', 'a', encoding='utf-8')
sys.stdout = error_to_file


app =  QtWidgets.QApplication(sys.argv)

#ДОБ. ШРИФТ
QtGui.QFontDatabase.addApplicationFontFromData(CousineRegular)
QtGui.QFontDatabase.addApplicationFontFromData(XpressiveBold)
QtGui.QFontDatabase.addApplicationFontFromData(AmazoneBt)
QtGui.QFontDatabase.addApplicationFontFromData(YouReGone)
QtGui.QFontDatabase.addApplicationFontFromData(Pollock2ctt)



FIRST = Zastavka()
WINDOW = Body()

#УДАЛЯЕМ ОБЪЕКТ ИЗ ПАМЯТИ
FIRST.setAttribute(QtCore.Qt.WA_DeleteOnClose, True)
FIRST.show()

def start_osn_window():
        FIRST.close()
        WINDOW.showMaximized()

QtCore.QTimer.singleShot(3000,start_osn_window)


error_to_file.close()
sys.exit(app.exec_())