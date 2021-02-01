#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on  05.09.2019

@author: Gubkin Leonid

Cinderella - Mass Text Editor

"""

from PySide2 import QtWidgets, QtGui, QtCore
from files.text_editors.techfunction import title_project,upload_options,save_options, files_on_folder
import sys
import random

from files.body_table import Body_Table 
from files.motor.mechanika import Mechanika
from files.motor.logview import LogView
from files.pics.header_l import Header_L
from files.pics.about import About
from files.pics.browse import Browse
from files.pics.exit import Exit
from files.pics.log import Log
from files.pics.test import Test
from files.pics.close import Close
from files.pics.start import Start
from files.pics.icon import Icon
from files.pics.img_header_1 import img_Header_Img_1
from files.pics.img_header_2 import img_Header_Img_2
from files.pics.img_header_3 import img_Header_Img_3
from files.pics.img_header_4 import img_Header_Img_4
from files.pics.img_header_5 import img_Header_Img_5
from files.mouse_paint import Drawer
from files.table_coding import Table_Coding



class Body(QtWidgets.QWidget):
    def __init__(self,parent=None):
        QtWidgets.QWidget.__init__(self,parent)
        img_icon = QtGui.QImage()
        img_icon.loadFromData(Icon)
        self.setWindowIcon(QtGui.QIcon(QtGui.QPixmap.fromImage(img_icon)))
        self.setWindowTitle(title_project)
        self.setWindowFlags(QtCore.Qt.Window)
        self.setMinimumSize(800,600)
        self.setStyleSheet("""
                           QWidget{ 
                           background-color: #24313c;
                           color : #8e949a;
                           }
                           QComboBox{
                           background-color: #24313c;
                           border-style: solid;
                           border-width: 2px;
                           border-color: gray;
                           border-radius: 5px;
                           }
                           QLineEdit#change_files{
                           border-style: solid;
                           border-width: 2px;
                           border-color: gray;
                           border-radius: 5px;
                           }
                           QTabWidget::pane#vkladki{
                           background-color: #24313c;
                           border-style: solid;
                           border-width: 2px;
                           border-color: gray;
                           border-radius: 5px;
                           border-top: 2px solid #C2C7CB;
                           }
                           QTabBar::tab {
                           background-color: #24313c;
                           border: 2px solid gray;
                           }
                           QGroupBox{
                           border-color: #ba6a6a;
                           color: #ba7a6a;
                           border: 2px solid gray;
                           border-radius: 5px;
                           height: 70px;
                           }
                           QGroupBox::title {
                           padding: 0px 5px;
                           }
                           QPushButton#button_change:enabled {
                           background-color: #f4c400;
                           border: 1px inset #000000;
                           border-radius: 5px;
                           color: #8e949a;
                           padding: 5px;
                           width: 80px;
                           }
                           QPushButton#button_change:hover {
                           background-color: #edb120;
                           border: 1px inset #000000;
                           border-radius: 5px;
                           color: #8e949a;
                           padding: 5px;
                           width: 80px;
                           }   
                           QPushButton#button_change:pressed{
                           background-color: #f47899;
                           border: 1px inset #000000;
                           border-radius: 5px;
                           color: #8e949a;
                           padding: 5px;
                           width: 80px;
                           }
                           QPushButton#button_change:disabled {
                           background-color: #dadfe4;
                           border: 1px inset #000000;
                           border-radius: 5px;
                           color: #101b15;
                           padding: 5px;
                           width: 80px;
                           }
                           
                           QPushButton#button_start:enabled {
                           background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 #44fd8d, stop:1 #ff45ba);
                           border: 1px inset #000000;
                           border-radius: 5px;
                           color: #101b15;
                           padding: 5px;
                           width: 80px;
                           height: 30px;
                           }
                           QPushButton#button_start:hover {
                           background-color: #44fd8d;
                           border: 1px inset #000000;
                           border-radius: 5px;
                           color: #101b15;
                           padding: 5px;
                           width: 80px;
                           }   
                           QPushButton#button_start:pressed{
                           background-color: #00f17c;
                           border: 1px inset #000000;
                           border-radius: 5px;
                           color: #101b15;
                           padding: 5px;
                           width: 80px;
                           }
                           QPushButton#button_stop:enabled {
                           background-color: #ff45ba;
                           border: 1px inset #000000;
                           border-radius: 5px;
                           color: #101b15;
                           padding: 5px;
                           width: 80px;
                           }
                           QPushButton#button_stop:hover {
                           background-color: #ff4583;
                           border: 1px inset #000000;
                           border-radius: 5px;
                           color: #101b15;
                           padding: 5px;
                           width: 80px;
                           }   
                           QPushButton#button_stop:pressed{
                           background-color: #ff4519;
                           border: 1px inset #000000;
                           border-radius: 5px;
                           color: #101b15;
                           padding: 5px;
                           width: 80px;
                           }
    
                           QPushButton#button_test:enabled {
                           background-color: #86e4c7;
                           border: 1px inset #000000;
                           border-radius: 5px;
                           color: #101b15;
                           padding: 5px;
                           width: 65px;
                           }
                           QPushButton#button_test:hover {
                           background-color: #79d0b4;
                           border: 1px inset #000000;
                           border-radius: 5px;
                           color: #101b15;
                           padding: 5px;
                           width: 65px;
                           }   
                           QPushButton#button_test:pressed{
                           background-color: #68b291;
                           border: 1px inset #000000;
                           border-radius: 5px;
                           color: #101b15;
                           padding: 5px;
                           width: 65px;
                           }
                           QPushButton#button_log:enabled,#button_about:enabled {
                           background-color: #d6e3fc;
                           border: 1px inset #000000;
                           border-radius: 5px;
                           color: #101b15;
                           padding: 5px;
                           width: 80px;
                           }
                           QPushButton#button_log:hover,#button_about:hover {
                           background-color: #edb120;
                           border: 1px inset #000000;
                           border-radius: 5px;
                           color: #101b15;
                           padding: 5px;
                           width: 80px;
                           }   
                           QPushButton#button_log:pressed,#button_about:pressed{
                           background-color: #b8fdd3;
                           border: 1px inset #000000;
                           border-radius: 5px;
                           color: #101b15;
                           padding: 5px;
                           width: 80px;
                           }
                           QPushButton#button_log:disabled,#button_about:disabled {
                           background-color: #dadfe4;
                           border: 1px inset #000000;
                           border-radius: 5px;
                           color: #101b15;
                           padding: 5px;
                           width: 80px;
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
                           
                           QProgressBar {
                           background-color: #05B8CC;
                           color: #f5c500;
                           font-size: 30px;
                           font-family: Xpressive;
                           border-radius: 5px;
                           text-align: center;
                           height: 50px;
                           }
                               
        
        
                           QToolTip { 
                           background-color: yellow; 
                           color: black; 
                           border: black solid 1px}
                           
                            """)
     
        #ЗАГРУЖАЕМ НАСТРОЙКИ ФАЙЛ settings.json
        self.all_file_options = upload_options()
        #ДЛЯ СТАТУС ДЛЯ КНОПКИ OK и CANCEL
        #(ЕСЛИ БЫЛА НАЖАТА КНОПКА CANCEL КНОПКА OK НЕ ПОЯВИТСЯ)
        self.result_stop = 0
        #СМОТРИМ СУЩЕСТВУЕТ ЛИ ФАЙЛ settings.json
        if len(self.all_file_options) == 0:
            result = QtWidgets.QMessageBox.critical(self,'Файл настроек не найден или поврежден','Внимание файл настроек settings.json не найден или поврежден. Дальнейшая работа программы не возможна!',buttons = QtWidgets.QMessageBox.Ok)
            if result == 1024:
                sys.exit()

        vertical_box_all = QtWidgets.QVBoxLayout()
        #HEADER
        gorizont_box_0 = QtWidgets.QHBoxLayout()
        vertical_box_all.addLayout(gorizont_box_0)
        #HEADER LEFT
        header_l = QtWidgets.QLabel()
        header_l.setSizePolicy(QtWidgets.QSizePolicy.Minimum,QtWidgets.QSizePolicy.Minimum)
        img_header_l = QtGui.QImage()
        img_header_l.loadFromData(Header_L)
        header_l.setPixmap(QtGui.QPixmap.fromImage(img_header_l))
        header_l.setAlignment(QtCore.Qt.AlignLeft)
        gorizont_box_0.addWidget(header_l,alignment=QtCore.Qt.AlignLeft)
        #HEADER CENTER
        header_с = Drawer()
        gorizont_box_0.addWidget(header_с,alignment=QtCore.Qt.AlignHCenter)
        header_с.setSizePolicy(QtWidgets.QSizePolicy.Maximum,QtWidgets.QSizePolicy.Maximum)


        #HEADER RIGHT
        header_r = QtWidgets.QLabel()
        header_r.setSizePolicy(QtWidgets.QSizePolicy.Minimum,QtWidgets.QSizePolicy.Minimum)
        img_header_r = QtGui.QImage()
        #ВЫБИРАЕМ СЛУЧАЙНУЮ КАРТИНКУ
        Header_R = random.choice([img_Header_Img_1,img_Header_Img_2,img_Header_Img_3,img_Header_Img_4,img_Header_Img_5])
        img_header_r.loadFromData(Header_R)
        header_r.setPixmap(QtGui.QPixmap.fromImage(img_header_r))
        header_r.setAlignment(QtCore.Qt.AlignLeft)
        gorizont_box_0.addWidget(header_r,alignment=QtCore.Qt.AlignRight)


        #CHANGE FILES
        gorizont_box_3 = QtWidgets.QHBoxLayout()
        vertical_box_all.addLayout(gorizont_box_3)
        
        group_box_3 = QtWidgets.QGroupBox('change folder: ')
        group_box_3.setToolTip('Выберите папку с файлом(ами) *.txt для редактирования')
        group_box_3.setFont(QtGui.QFont('Xpressive',11))
        gorizont_box_3.addWidget(group_box_3)
        gorizont_box_5 = QtWidgets.QHBoxLayout()
        gorizont_box_5.setSpacing(1)
        group_box_3.setLayout(gorizont_box_5)
        self.change_files = QtWidgets.QLineEdit()
        self.change_files.setObjectName('change_files')
        self.change_files.setText(self.all_file_options['browse'])
        self.change_files.setReadOnly(True)
        self.change_files.setMaxLength(100)
        #ВЫБИРАЕМ ПАПКУ С ФАЙЛАМИ
        def path_folder_wih_files():
            dir_with_flies = QtWidgets.QFileDialog.getExistingDirectory(parent = self,directory = self.all_file_options['browse'])
            if bool(dir_with_flies) == True:   
                self.change_files.setText(dir_with_flies)
                #LCD ЗАДАЕМ ЗНАЧЕНИЕ
                lcd_search_files.display(len(files_on_folder(dir_with_flies)))
                #STATUSBAR ЗАДАЕМ ЗНАЧЕНИЕ
                progress.setRange(0,len(files_on_folder(dir_with_flies)))

            
        button_change = QtWidgets.QPushButton('browse')
        button_change.setObjectName('button_change')
        button_change.setFont(QtGui.QFont('Xpressive',15))
        img_button_change = QtGui.QImage()
        img_button_change.loadFromData(Browse)
        button_change.setIcon(QtGui.QIcon(QtGui.QPixmap.fromImage(img_button_change)))
        button_change.clicked.connect(path_folder_wih_files)
        gorizont_box_5.addWidget(button_change)
        gorizont_box_5.addWidget(self.change_files)


        #КОДИРОВКА
        group_box_8 = QtWidgets.QGroupBox()
        group_box_8.setFont(QtGui.QFont('Xpressive',11))
        group_box_8.setToolTip('Выберите кодировку ваших файлов')
        gorizont_box_3.addWidget(group_box_8)
        gorizont_box_6 = QtWidgets.QHBoxLayout()
        gorizont_box_6.setSpacing(1)
        group_box_8.setLayout(gorizont_box_6)
        self.cod_table = Table_Coding()
        self.cod_table.table.setCurrentText(self.all_file_options['coding'])
        gorizont_box_6.addWidget(self.cod_table)

        
        #BACKUP OPTIONS
        group_box_6 = QtWidgets.QGroupBox('backup?')
        group_box_6.setFont(QtGui.QFont('Xpressive',11))
        group_box_6.setToolTip('Делать ли резервные копии файлов, до редактирования')
        gorizont_box_3.addWidget(group_box_6)
        gorizont_box_7 = QtWidgets.QHBoxLayout()
        gorizont_box_7.setSpacing(1)
        group_box_6.setLayout(gorizont_box_7)
        radio_button_1 = QtWidgets.QRadioButton('yes')
        radio_button_1.setStyleSheet('color: green;')
        radio_button_1.setFont(QtGui.QFont('Xpressive',15))
        radio_button_2 = QtWidgets.QRadioButton('no')
        radio_button_2.setStyleSheet('color: red;')
        radio_button_2.setFont(QtGui.QFont('Xpressive',15))
        radio_button_2.setChecked(True)
        gorizont_box_7.addWidget(radio_button_1)
        gorizont_box_7.addWidget(radio_button_2)
        
        
        #LCD КОЛИЧЕСТВО ФАЙЛОВ
        group_box_5 = QtWidgets.QGroupBox()
        group_box_5.setFont(QtGui.QFont('Xpressive'))
        group_box_5.setToolTip('Найдено файлов с разрешением *.txt, в выбранной папке')
        gorizont_box_3.addWidget(group_box_5)
        gorizont_box_6 = QtWidgets.QHBoxLayout()
        gorizont_box_6.setSpacing(1)
        group_box_5.setLayout(gorizont_box_6)
        lcd_search_files = QtWidgets.QLCDNumber(5)
        lcd_search_files.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        
        lcd_search_files.display(len(files_on_folder(self.change_files.text())))
        gorizont_box_6.addWidget(lcd_search_files)
        
        
        vkladki = QtWidgets.QTabWidget()
        vkladki.setObjectName('vkladki')
        #ONE PAGE
        two_tables = Body_Table()
        vkladki.addTab(two_tables,'File Type: *.txt')
        vkladki.setFont(QtGui.QFont('pollock2ctt',12))
        vkladki.setCurrentIndex(0)
        vertical_box_all.addWidget(vkladki)
        gorizont_box = QtWidgets.QHBoxLayout()
        vertical_box_all.addLayout(gorizont_box)
        #BUTTONS
        group_box = QtWidgets.QGroupBox()
        gorizont_box.addWidget(group_box)
        gorizont_box_1 = QtWidgets.QHBoxLayout()
        group_box.setLayout(gorizont_box_1)
        button_start = QtWidgets.QPushButton('Start')
        button_start.setObjectName('button_start')
        button_start.setFont(QtGui.QFont("You're Gone",15))
        button_start.setToolTip('Запуск процесса редактирования файлов')
        button_test = QtWidgets.QPushButton('Test')
        button_test.setObjectName('button_test')
        button_test.setToolTip('Просмотр результата редактирования файлов, на примере одного файла (сам файл не изменяется)')
        button_test.setFont(QtGui.QFont("You're Gone",15))
        
        #МЕНЯЕМ ЦВЕТ И ТЕКСТ КНОПКИ
        def eff_dutton_test_on():
            button_test.setText('Wait')
            button_test.setStyleSheet('background-color: #68b291')
           
        button_test.pressed.connect(eff_dutton_test_on)
        
        #МЕНЯЕМ ЦВЕТ И ТЕКСТ КНОПКИ
        def eff_dutton_test_off():
            button_test.setText('Test')
            button_test.setStyleSheet('background-color: #86e4c7')

        button_test.released.connect(eff_dutton_test_off)
        
        
        img_button_test = QtGui.QImage()
        img_button_test.loadFromData(Test)
        button_test.setIcon(QtGui.QIcon(QtGui.QPixmap.fromImage(img_button_test)))
        
        
        img_button_start = QtGui.QImage()
        img_button_start.loadFromData(Start)
        button_start.setIcon(QtGui.QIcon(QtGui.QPixmap.fromImage(img_button_start)))
        button_stop = QtWidgets.QPushButton('Stop')
        button_stop.setObjectName('button_stop')
        button_stop.setFont(QtGui.QFont("You're Gone",15))
        
        img_button_stop = QtGui.QImage()
        img_button_stop.loadFromData(Close)
        button_stop.setIcon(QtGui.QIcon(QtGui.QPixmap.fromImage(img_button_stop)))

        
        
        self.mythread = Mechanika(self)
        
        #СИГНАЛ ЧТО ФАЙЛОВ В ПАПКЕ НЕТ
        def not_files():
            self.change_files.setStyleSheet('background-color: red;')
            result = QtWidgets.QMessageBox.information(self,'Папка с файлами не выбрана или ...','Папка с файлами не выбрана или в текущей папке нет файлов txt',defaultButton = QtWidgets.QMessageBox.Ok)
            if result == 1024:
                self.change_files.setStyleSheet('background-color: #24313c;')


        #СИГНАЛ ЕСЛИ В ПРАВОЙ ТАБЛИЦЕ ПУСТО
        def right_table_pusto():
            two_tables.right_table.setStyleSheet('QWidget#right_table {background-color: red;}')
            result = QtWidgets.QMessageBox.information(self,'Не выбран модуль(и)','Выберите модуль(и) для обработки текста',defaultButton = QtWidgets.QMessageBox.Ok)
            if result == 1024:
                two_tables.right_table.setStyleSheet('QWidget#right_table {background-color: #24313c;}')
    
    
        
        #КНОПКА СТАРТ
        def on_start():
            #ДЛЯ СТАРТА ПЕРИФЕРИЙНЫХ МОДУЛЕЙ
            Mechanika.stop_now = True
            #ДЛЯ СТАТУС ДЛЯ КНОПКИ OK и CANCEL
            self.result_stop = 0
            #ЕСЛИ ФАЙЛОВ В ПАПКЕ НЕТ
            if lcd_search_files.value() == 0:
                not_files()
            #ЕСЛИ В ПРАВОЙ ТАБЛИЦЕ ПУСТО
            if two_tables.MODEL_R.rowCount() == 0:
                right_table_pusto()  
            else:
                #ПУТЬ ПАПКИ С ФАЙЛАМИ ДЛЯ ОБРАБОТКИ
                self.mythread.files_on_folder(self.change_files.text())
                #BACKUP STATUS
                self.mythread.backup_yes_or_no(radio_button_1.isChecked())
                #КОДИРОВКА
                self.mythread.cur_coding = self.cod_table.table.currentText()
                #СПИСОК ФУНКЦИЙ ДЛЯ ОБРАБОТКИ ТЕКСТА
                list_func = two_tables.editors_list()
                self.mythread.funcs_to_mechanika(list_func)
                if not self.mythread.isRunning():
                    self.mythread.start()
                    gorizont_box_1.replaceWidget(button_start,button_stop)
                    button_start.setHidden(True)
                    button_log.setStyleSheet('background-color: #e5f389')
                    button_stop.setHidden(False)
                    #УБРАЕМ КЛИКАБЕЛЬНОСТЬ
                    group_box_3.setEnabled(False)
                    group_box_6.setEnabled(False)
                    group_box7.setEnabled(False)
                    group_box_8.setEnabled(False)
                    button_test.setEnabled(False)
                    vkladki.setEnabled(False)
                    
        
        
        #ВОЗВРАЩАЕМ ЭЛЕМЕНТАМ КЛИКАБЕЛЬНОСТЬ
        def clickable_elm():
            button_start.setHidden(False)
            button_stop.setHidden(True)
            group_box_3.setEnabled(True)
            group_box_6.setEnabled(True)
            group_box7.setEnabled(True)
            group_box_8.setEnabled(True)
            button_test.setEnabled(True)
            vkladki.setEnabled(True)


            
        #КНОПКА СТОП
        def on_stop():
            self.mythread.running = False
            #ДЛЯ ОСТАНОВКИ ПЕРИФЕРИЙНЫХ МОДУЛЕЙ
            Mechanika.stop_now = False
            gorizont_box_1.replaceWidget(button_stop,button_start)
            clickable_elm()
            #СООБЩЕНИЕ ОБ ОКОНЧАНИИ
            self.result_stop = 1
            QtWidgets.QMessageBox.information(self,'Stop','Остановленно',defaultButton = QtWidgets.QMessageBox.Ok)
            
        
        #СТАТУС
        def on_change():
            gorizont_box_1.replaceWidget(button_stop,button_start)
            clickable_elm()
            #КРАСИМ КНОПКУ LOG
            for i in self.mythread.log:
                if i.endswith('[Error]</b>') == True:
                    button_log.setStyleSheet('background-color: red;')
                    break
            if not self.result_stop == 1:
                #СООБЩЕНИЕ ОБ ОКОНЧАНИИ
                QtWidgets.QMessageBox.information(self,'Ok','Выполнено',defaultButton = QtWidgets.QMessageBox.Ok)

            
        #ДЛЯ ИЗМЕНЕНИЯ ЗНАЧЕНИЯ СТАТУСБАРА
        def new_value_statusbar(int):
            progress.setValue(int)
            
        self.mythread.value_statusbar.connect(new_value_statusbar,QtCore.Qt.QueuedConnection)
        self.mythread.mysignal.connect(on_change,QtCore.Qt.QueuedConnection)  
        button_start.clicked.connect(on_start)
        button_stop.clicked.connect(on_stop)
        
        
        #КНОПКА ТЕСТ
        def on_test():
            #ЕСЛИ ФАЙЛОВ В ПАПКЕ НЕТ
            if lcd_search_files.value() == 0:
                not_files()
            else:
                #ПУТЬ ПАПКИ С ФАЙЛАМИ ДЛЯ ОБРАБОТКИ
                self.mythread.files_on_folder(self.change_files.text())
                #КОДИРОВКА
                self.mythread.cur_coding = self.cod_table.table.currentText()
                #СПИСОК ФУНКЦИЙ ДЛЯ ОБРАБОТКИ ТЕКСТА
                list_func = two_tables.editors_list()
                self.mythread.funcs_to_mechanika(list_func)
                self.mythread.test_edit()
        
        
        button_test.clicked.connect(on_test)

        
        gorizont_box_1.addWidget(button_start,alignment = QtCore.Qt.AlignVCenter)
        gorizont_box_1.addWidget(button_test,alignment = QtCore.Qt.AlignVCenter)

        #STATUSBAR
        group_box_1 = QtWidgets.QGroupBox()
        gorizont_box.addWidget(group_box_1)
        gorizont_box_2 = QtWidgets.QHBoxLayout()
        group_box_1.setLayout(gorizont_box_2)
        progress = QtWidgets.QProgressBar()
        progress.setObjectName('progress')
        gorizont_box_2.addWidget(progress)
        progress.setRange(0,lcd_search_files.intValue())
        #HELP AND ABOUT
        group_box7 = QtWidgets.QGroupBox()
        gorizont_box.addWidget(group_box7)
        gorizont_box_10 = QtWidgets.QHBoxLayout()
        group_box7.setLayout(gorizont_box_10)
        button_log = QtWidgets.QPushButton('Log')
        button_log.setObjectName('button_log')
        button_log.setToolTip('Посмотреть лог файл процесса редактирования файлов')
        button_log.setFont(QtGui.QFont("You're Gone",15))
        
        img_button_log = QtGui.QImage()
        img_button_log.loadFromData(Log)
        button_log.setIcon(QtGui.QIcon(QtGui.QPixmap.fromImage(img_button_log)))
        button_about = QtWidgets.QPushButton('About')
        button_about.setObjectName('button_about')
        button_about.setToolTip('Настройка и описание программы')
        button_about.setFont(QtGui.QFont("You're Gone",15))
        
        img_button_about = QtGui.QImage()
        img_button_about.loadFromData(About)
        button_about.setIcon(QtGui.QIcon(QtGui.QPixmap.fromImage(img_button_about)))
        button_close = QtWidgets.QPushButton('Close')
        button_close.setObjectName('button_close')
        button_close.setToolTip('Выход из программы')
        button_close.setFont(QtGui.QFont("You're Gone",15))
        
        img_button_close = QtGui.QImage()
        img_button_close.loadFromData(Exit)
        button_close.setIcon(QtGui.QIcon(QtGui.QPixmap.fromImage(img_button_close)))
        
        itslog = LogView(self)
        
        #ДЛЯ ОТОБРАЖЕНИЯ LOGa
        def log_view():
            itslog.add_log_info(self.mythread.log)
            itslog.showMaximized()
            
        button_log.clicked.connect(log_view)
        #ДЛЯ ОТОБРАЖЕНИЯ ABOUT
        def about_view():
            about_title = 'Cinderella | About'
            about_text = '''
        <p style="color:grey;font-size: 17px;font-family: pollock2ctt;"> <b style="color:#E5F993;">Cinderella</b> - небольшая программа для массовой обработки текстовых файлов</p>

        <p style="color:grey;font-size: 15px;font-family: pollock2ctt;">версия: 1.5</p>

        <p style="color:grey;font-size: 15px;font-family: pollock2ctt;">лицензия: Donationware</p>

        <p style="color:grey;font-size: 15px;font-family: pollock2ctt;">donate: <a style="color:#C6D8AF;font-size: 15px;font-family: Xpressive;" href="https://gubkin-utility.github.io/cinderella/page/donate.html">Donation Link </a></p>

        <p style="color:grey;font-size: 15px;font-family: pollock2ctt;">автор: <a style="color:orange;font-size: 15px;font-family: Xpressive;" href="https://www.facebook.com/leonid.gubkin">Leonid Gubkin</a></p>

        <p style="color:grey;font-size: 15px;font-family: pollock2ctt;">сайт: <a style="color:#F9DC5C;font-size: 15px;font-family: Xpressive;" href="https://gubkin-utility.github.io/cinderella/">Cinderella Web</a></p>

        <p  style="color:grey;font-size: 15px;font-family: pollock2ctt;">This program comes with absolutely no warranty<br>(эта программа не имеет никаких гарантий)</p>
        '''
            QtWidgets.QMessageBox.about(self,about_title,about_text)

            
        button_about.clicked.connect(about_view)
            
        button_close.clicked.connect(lambda: self.close())
        
        gorizont_box_10.addWidget(button_log)
        gorizont_box_10.addWidget(button_about)
        gorizont_box_10.addWidget(button_close)
        #ПУСТОЕ МЕСТО
        pusto = QtWidgets.QVBoxLayout()
        pusto.addSpacing(30)
        
        vertical_box_all.addLayout(pusto)

        self.setLayout(vertical_box_all)
        
    #ПЕРЕХВАТ ЗАКРЫТИЯ ОКНА    
    def closeEvent(self,e):
        #ОСТАНАВЛИВАЕМ ПОТОК ЕСЛИ ОН НЕ БЫЛ ОСТАНОВЛЕН
        self.hide()
        self.mythread.running = False
        self.mythread.wait(5000)
        #СОХРАНЯЕМ НАСТРОЙКИ
        self.all_file_options = upload_options()
        self.all_file_options['browse'] = self.change_files.text()
        self.all_file_options['coding'] = self.cod_table.table.currentText()
        save_options(self.all_file_options)
        
        QtWidgets.QApplication.closeAllWindows()
        e.accept()
        
        


if __name__ == '__main__':
    app =  QtWidgets.QApplication(sys.argv)
    window = Body()
    window.show()
    sys.exit(app.exec_())
