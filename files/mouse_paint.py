#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on  05.09.2019

@author: Gubkin Leonid

Cinderella - Mass Text Editor

"""

import sys
from PySide2.QtWidgets import (QApplication, QLabel, QWidget,QVBoxLayout)
from PySide2.QtGui import QColor, QPainter, QPainterPath, QPen
from PySide2.QtCore import Qt,QPoint,QSize
from PySide2.QtGui import QPainter
from PySide2.QtCore import Signal
from PySide2.QtWidgets import QApplication



class Drawer(QWidget):
    newPoint = Signal(QPoint)
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self.path = QPainterPath()    

    def paintEvent(self, event):
        kist = QPen()
        kist.setColor(QColor('Yellow'))
        kist.setWidth(2)
        kist.setJoinStyle(Qt.RoundJoin)
        painter = QPainter(self)
        painter.setPen(kist)
        painter.drawPath(self.path)

    def mousePressEvent(self, event):
        self.path.moveTo(event.pos())
        self.update()

    def mouseMoveEvent(self, event):
        self.path.lineTo(event.pos())
        self.newPoint.emit(event.pos())
        self.update()

    def sizeHint(self):
        return QSize(self.size().width()*2, self.size().height()//3)


class MyWidget(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self.setLayout(QVBoxLayout())
        label = QLabel(self)
        drawer = Drawer(self)
        self.layout().addWidget(label)
        self.layout().addWidget(drawer)




if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MyWidget()
    w.show()
    sys.exit(app.exec_())
