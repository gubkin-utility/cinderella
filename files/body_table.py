#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on  05.09.2019

@author: Gubkin Leonid

Cinderella - Text Editor

"""

from PyQt5 import QtWidgets, QtGui, QtCore
import sys, os
from files.add_editors import all_editors


class Body_Table(QtWidgets.QWidget):
    def __init__(self,parent=None):
        QtWidgets.QFrame.__init__(self,parent)
        gorizont_box = QtWidgets.QHBoxLayout()
        #ЛЕВАЯ ТАБЛИЦА
        left_table = QtWidgets.QListView()
        MODEL_L = QtGui.QStandardItemModel(parent = self)
        left_table.setModel(MODEL_L)
        left_table.setViewMode(0)
        left_table.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        left_table.setDragDropMode(1)
        left_table.setAlternatingRowColors(True)
        left_table.setTextElideMode(1)
        left_table.setWrapping(False)
        left_table.setResizeMode(0)
        
        for i in sorted(all_editors.keys()):
            MODEL_L.appendRow([QtGui.QStandardItem(i)])

        #ПРАВАЯ ТАБЛИЦА
        right_table = QtWidgets.QListView()
        self.MODEL_R = QtGui.QStandardItemModel(parent = self)
        right_table.setModel(self.MODEL_R)
        right_table.setViewMode(0)
        right_table.setDragEnabled(True)
        right_table.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        right_table.setDragDropMode(2)
        right_table.setTextElideMode(1)
        right_table.setWrapping(False)
        right_table.setResizeMode(0)
        
        def its_element(d):
            all_editors.get(d.data())[0]()
        
        
        #МЕНЯЕМ ЦВЕТ ЕСЛИ У МОДУЛЯ НЕТ НАСТРОЕК 
        def tabletotable(d):
            if all_editors.get(d.text())[2] == False:
                d.setBackground(QtGui.QBrush(QtGui.QColor('#1def6f')))
            
        
        right_table.doubleClicked.connect(its_element)
        self.MODEL_R.itemChanged.connect(tabletotable)
        
        #КНОПКИ ДЛЯ УПРАВЛЕНИЯ ТАБЛИЦЕЙ
        vertical_box_1 = QtWidgets.QVBoxLayout()
        group_box = QtWidgets.QGroupBox()
        vertical_box_1.addWidget(group_box,alignment = QtCore.Qt.AlignRight)
        vertical_box_2 = QtWidgets.QVBoxLayout()
        group_box.setLayout(vertical_box_2)
        
        right_table.setLayout(vertical_box_1)
        button_up = QtWidgets.QPushButton()
        button_up.setToolTip('вверх')
        button_up.setIcon(QtGui.QIcon(os.path.join('.','files','pic','table_up.png')))
        button_up.setStyleSheet('background-color: #b3ecec;')
        button_up.setMaximumSize(30,30)
        #ВВЕРХ ПО ТАБЛИЦЕ
        def up_action_button():
            if self.activerownow == None:
                None
            else:
                res = self.MODEL_R.takeRow(self.activerownow)
                self.activerownow -= 1
                if self.activerownow == -1:
                    self.activerownow = 0
                
                self.MODEL_R.insertRow(self.activerownow,res)
                if self.activerownow != None:
                    #ВЫДЕЛЯЕМ СТРОКУ
                    right_table.setCurrentIndex(res[0].index())

            
        button_up.clicked.connect(up_action_button)
        #ВНИЗ ПО ТАБЛИЦЕ
        button_down = QtWidgets.QPushButton()
        button_down.setToolTip('вниз')
        button_down.setIcon(QtGui.QIcon(os.path.join('.','files','pic','table_down.png')))
        button_down.setStyleSheet('background-color: #b3ecec;')
        button_down.setMaximumSize(30,30)
        def down_action_button():
            if self.activerownow == None:
                None
            else:
                all_row = self.MODEL_R.rowCount()
                res = self.MODEL_R.takeRow(self.activerownow)
                self.activerownow += 1
                if self.activerownow == all_row:
                    self.activerownow = all_row - 1
                self.MODEL_R.insertRow(self.activerownow,res)
                if self.activerownow != None:
                    #ВЫДЕЛЯЕМ СТРОКУ
                    right_table.setCurrentIndex(res[0].index())

        button_down.clicked.connect(down_action_button)
        #КНОПКА ОЧИСТИТЬ ВСЕ
        button_clear = QtWidgets.QPushButton()
        button_clear.setToolTip('очистить все')
        button_clear.setIcon(QtGui.QIcon(os.path.join('.','files','pic','clear_all.png')))
        button_clear.setStyleSheet('background-color: #b3ecec;')
        button_clear.setMaximumSize(30,30)
        button_clear.clicked.connect(lambda:self.MODEL_R.clear())
        #КНОПКА УДАЛИТЬ СТРОКУ
        button_delete = QtWidgets.QPushButton()
        button_delete.setToolTip('удалить')
        button_delete.setIcon(QtGui.QIcon(os.path.join('.','files','pic','delete.png')))
        button_delete.setStyleSheet('background-color: #b3ecec;')
        #АКТИВНАЯ СТРОКА
        self.activerownow = None
        #УДАЛЕНИЕ СТРОКИ ИЗ ТАБЛИЦ
        def delete_row():
            if self.activerownow == None:
                None
            else:
                self.MODEL_R.removeRow(self.activerownow)
                self.activerownow = None
                right_table.clearSelection()
                
        #КНОПКА УДАЛИТЬ СТРОКУ  
        button_delete.clicked.connect(delete_row)
        #ОПРЕДЕЛЯЕМ АКТИВНУЮ СТРОКУ
        def its_row_now(d):
            self.activerownow = d.row()
        #ОПРЕДЕЛЯЕМ АКТИВНУЮ СТРОКУ
        right_table.clicked.connect(its_row_now)

        
        button_delete.setMaximumSize(30,30)

        vertical_box_2.addWidget(button_up)
        vertical_box_2.addWidget(button_down)
        vertical_box_2.addWidget(button_delete)
        vertical_box_2.addWidget(button_clear)
        group_box.setSizePolicy(QtWidgets.QSizePolicy.Maximum,QtWidgets.QSizePolicy.Maximum)

        gorizont_box.addWidget(left_table)
        gorizont_box.addWidget(right_table)
        self.setLayout(gorizont_box)

    
    #ПОЛУЧАЕМ СПИСОК ИЗ ПРАВОЙ ТАБЛИЦЫ
    def editors_list(self):
        all_editor_for_work = []
        for i in range(self.MODEL_R.rowCount()):
                #ПОЛУЧАЕМ ССЫЛКУ НА ЭЛЕМЕНТ
                link_element = self.MODEL_R.item(i)
                text_element = link_element.text()
                dd = all_editors.get(text_element)
                all_editor_for_work.append(dd[1])
        return all_editor_for_work    
                    


        
if __name__ == '__main__':
    app =  QtWidgets.QApplication(sys.argv)
    window = Body_Table()
    window.show()
    sys.exit(app.exec_())
