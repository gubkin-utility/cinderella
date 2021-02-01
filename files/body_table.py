#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on  05.09.2019

@author: Gubkin Leonid

Cinderella - Mass Text Editor

"""

from PySide2 import QtWidgets, QtGui, QtCore
import sys
from files.add_editors import all_editors
from files.pics.table_up import Table_Up
from files.pics.table_down import Table_Down
from files.pics.delete import Delete
from files.pics.clear_all import Clear_All


    

class Body_Table(QtWidgets.QWidget):
    def __init__(self,parent=None):
        QtWidgets.QWidget.__init__(self,parent)
        self.setStyleSheet("""
                           QWidget { 
                           background-color: #24313c;
                           color : #8e949a;
                           }
                           QPushButton#button_up:enabled,#button_down:enabled {
                           background-color: #0ad49e;
                           border: 1px inset #000000;
                           border-radius: 5px;
                           color: #0ad49e;
                           padding: 5px;
                           }
                           QPushButton#button_up:hover,#button_down:hover {
                           background-color: #0affe6;
                           border: 1px inset #000000;
                           border-radius: 5px;
                           color: #8e949a;
                           padding: 5px;
                           }   
                           QPushButton#button_up:pressed,#button_down:pressed{
                           background-color: #93fce6;
                           border: 1px inset #000000;
                           border-radius: 5px;
                           color: #8e949a;
                           padding: 5px;
                           }
                           QPushButton#button_up:disabled,#button_down:disabled {
                           background-color: #f4f1e6;
                           border: 1px inset #000000;
                           border-radius: 5px;
                           color: #101b15;
                           padding: 5px;
                           }
                           
                           QPushButton#button_delete:enabled {
                           background-color: #fe9256;
                           border: 1px inset #000000;
                           border-radius: 5px;
                           color: #0ad49e;
                           padding: 5px;
                           }
                           QPushButton#button_delete:hover {
                           background-color: #fea656;
                           border: 1px inset #000000;
                           border-radius: 5px;
                           color: #8e949a;
                           padding: 5px;
                           }   
                           QPushButton#button_delete:pressed{
                           background-color: #fecb98;
                           border: 1px inset #000000;
                           border-radius: 5px;
                           color: #8e949a;
                           padding: 5px;
                           }
                           QPushButton#button_delete:disabled {
                           background-color: #f4f1e6;
                           border: 1px inset #000000;
                           border-radius: 5px;
                           color: #101b15;
                           padding: 5px;
                           }

                           QPushButton#button_clear:enabled {
                           background-color: #ff50ba;
                           border: 1px inset #000000;
                           border-radius: 5px;
                           color: #0ad49e;
                           padding: 5px;
                           }
                           QPushButton#button_clear:hover {
                           background-color: #ff78ba;
                           border: 1px inset #000000;
                           border-radius: 5px;
                           color: #8e949a;
                           padding: 5px;
                           }   
                           QPushButton#button_clear:pressed{
                           background-color: #ffa0ba;
                           border: 1px inset #000000;
                           border-radius: 5px;
                           color: #8e949a;
                           padding: 5px;
                           }
                           QPushButton#button_clear:disabled {
                           background-color: #f4f1e6;
                           border: 1px inset #000000;
                           border-radius: 5px;
                           color: #101b15;
                           padding: 5px;
                           }


                            """)
        gorizont_box = QtWidgets.QHBoxLayout()
        #ЛЕВАЯ ТАБЛИЦА
        left_table = QtWidgets.QListView()
        MODEL_L = QtGui.QStandardItemModel(parent = self)
        left_table.setModel(MODEL_L)
        left_table.setViewMode(QtWidgets.QListView.ViewMode.ListMode)
        left_table.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        left_table.setDragDropMode(QtWidgets.QAbstractItemView.DragDropMode.DragOnly)
        left_table.setTextElideMode(QtCore.Qt.TextElideMode.ElideRight)
        left_table.setWrapping(False)
        left_table.setResizeMode(QtWidgets.QListView.ResizeMode.Fixed)
        left_table.setFont(QtGui.QFont('pollock2ctt',15))

        
        for i in sorted(all_editors.keys()):
            MODEL_L.appendRow([QtGui.QStandardItem(i)])

        #ПРАВАЯ ТАБЛИЦА
        self.right_table = QtWidgets.QListView()
        self.right_table.setObjectName('right_table')
        self.MODEL_R = QtGui.QStandardItemModel(parent = self)
        self.right_table.setModel(self.MODEL_R)
        self.right_table.setViewMode(QtWidgets.QListView.ViewMode.ListMode)
        self.right_table.setDragEnabled(True)
        self.right_table.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.right_table.setDragDropMode(QtWidgets.QAbstractItemView.DragDropMode.DropOnly)
        self.right_table.setTextElideMode(QtCore.Qt.TextElideMode.ElideRight)
        self.right_table.setWrapping(False)
        self.right_table.setResizeMode(QtWidgets.QListView.ResizeMode.Fixed)
        self.right_table.setMouseTracking(True)
        self.right_table.setFont(QtGui.QFont('pollock2ctt',15))
        
        def its_element(d):
            all_editors.get(d.data())[0](self)
        
        
        #МЕНЯЕМ ЦВЕТ ЕСЛИ У МОДУЛЯ НЕТ НАСТРОЕК 
        def tabletotable(d):
            if all_editors.get(d.text())[2] == False:
                d.setBackground(QtGui.QBrush(QtGui.QColor('#1def6f')))
            
        
        self.right_table.doubleClicked.connect(its_element)
        self.MODEL_R.itemChanged.connect(tabletotable)
        
        #ИЩЕМ ПОВТОРЫ В ТАБЛИЦЕ И УДАЛЯЕМ
        def test_on_duplicate():
            #ПОЛУЧАЕМ ССЫЛКУ НА ЭЛЕМЕНТ
            if self.MODEL_R.rowCount() > 1:
                link_element = self.MODEL_R.item(self.MODEL_R.rowCount()-1)
                text_element = link_element.text()
                if len(self.MODEL_R.findItems(text_element,flags=QtCore.Qt.MatchExactly,column=0)) >= 2 and all_editors.get(text_element)[2] == True:
                    self.MODEL_R.removeRow(self.MODEL_R.rowCount()-1)
                    
        
        self.right_table.viewportEntered.connect(test_on_duplicate)
        
        #КНОПКИ ДЛЯ УПРАВЛЕНИЯ ТАБЛИЦЕЙ
        vertical_box_1 = QtWidgets.QVBoxLayout()
        group_box = QtWidgets.QGroupBox()
        vertical_box_1.addWidget(group_box,alignment = QtCore.Qt.AlignRight)
        vertical_box_2 = QtWidgets.QVBoxLayout()
        group_box.setLayout(vertical_box_2)
        
        self.right_table.setLayout(vertical_box_1)
        button_up = QtWidgets.QPushButton()
        button_up.setToolTip('вверх')
        button_up.setObjectName('button_up')
        img_button_up = QtGui.QImage()
        img_button_up.loadFromData(Table_Up)
        button_up.setIcon(QtGui.QIcon(QtGui.QPixmap.fromImage(img_button_up)))
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
                    self.right_table.setCurrentIndex(res[0].index())

            
        button_up.clicked.connect(up_action_button)
        #ВНИЗ ПО ТАБЛИЦЕ
        button_down = QtWidgets.QPushButton()
        button_down.setToolTip('вниз')
        button_down.setObjectName('button_down')
        img_button_down = QtGui.QImage()
        img_button_down.loadFromData(Table_Down)
        button_down.setIcon(QtGui.QIcon(QtGui.QPixmap.fromImage(img_button_down)))
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
                    self.right_table.setCurrentIndex(res[0].index())

        button_down.clicked.connect(down_action_button)
        #КНОПКА ОЧИСТИТЬ ВСЕ
        button_clear = QtWidgets.QPushButton()
        button_clear.setToolTip('очистить все')
        button_clear.setObjectName('button_clear')
        img_button_clear = QtGui.QImage()
        img_button_clear.loadFromData(Clear_All)
        button_clear.setIcon(QtGui.QIcon(QtGui.QPixmap.fromImage(img_button_clear)))
        button_clear.setMaximumSize(30,30)
        button_clear.clicked.connect(lambda:self.MODEL_R.clear())
        #КНОПКА УДАЛИТЬ СТРОКУ
        button_delete = QtWidgets.QPushButton()
        button_delete.setToolTip('удалить')
        button_delete.setObjectName('button_delete')
        img_button_delete = QtGui.QImage()
        img_button_delete.loadFromData(Delete)
        button_delete.setIcon(QtGui.QIcon(QtGui.QPixmap.fromImage(img_button_delete)))
        #АКТИВНАЯ СТРОКА
        self.activerownow = None
        #УДАЛЕНИЕ СТРОКИ ИЗ ТАБЛИЦ
        def delete_row():
            if self.activerownow == None:
                None
            else:
                self.MODEL_R.removeRow(self.activerownow)
                self.activerownow = None
                self.right_table.clearSelection()
                
        #КНОПКА УДАЛИТЬ СТРОКУ  
        button_delete.clicked.connect(delete_row)
        #ОПРЕДЕЛЯЕМ АКТИВНУЮ СТРОКУ
        def its_row_now(d):
            self.activerownow = d.row()
        #ОПРЕДЕЛЯЕМ АКТИВНУЮ СТРОКУ
        self.right_table.clicked.connect(its_row_now)

        
        button_delete.setMaximumSize(30,30)

        vertical_box_2.addWidget(button_up)
        vertical_box_2.addWidget(button_down)
        vertical_box_2.addWidget(button_delete)
        vertical_box_2.addWidget(button_clear)
        group_box.setSizePolicy(QtWidgets.QSizePolicy.Maximum,QtWidgets.QSizePolicy.Maximum)

        gorizont_box.addWidget(left_table)
        gorizont_box.addWidget(self.right_table)
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
