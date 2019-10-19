#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on  05.09.2019

@author: Gubkin Leonid

Cinderella - Text Editor

"""

from PyQt5 import QtWidgets, QtGui, QtCore, QtMultimedia
from files.text_editors.techfunction import title_project,icon_project,upload_options,save_options, files_on_folder
import sys, os

from files.body_table import Body_Table 
from files.motor.mechanika import Mechanika
from files.motor.logview import LogView

from files.about import About




class Body(QtWidgets.QWidget):
    def __init__(self,parent=None):
        QtWidgets.QFrame.__init__(self,parent)
        self.setWindowIcon(QtGui.QIcon(icon_project))
        self.setWindowTitle(title_project)
        self.setWindowFlags(QtCore.Qt.Window)
        self.resize(800,600)
#        self.setStyleSheet('background-color: #bae1ff; color : black;')
        self.setStyleSheet("""
                           QToolTip { 
                           background-color: yellow; 
                           color: black; 
                           border: black solid 1px}
                           QWidget{ 
                           background-color: #bae1ff;
                           color : black;}
                            """)
     
        #ЗАГРУЖАЕМ НАСТРОЙКИ ФАЙЛ settings.json
        self.all_file_options = upload_options()
        #МУЗЫКАЛЬНЫЙ ФРАГМЕНТ
        self.end_music = QtMultimedia.QSoundEffect()
        #ГРОМКОСТЬ
        self.end_music.setVolume(1)
        self.singl = QtCore.QUrl.fromLocalFile(os.path.join('.','files','sound','ok.wav'))
        self.end_music.setSource(self.singl)
        #СКОЛЬКО РАЗ ПОВТОРИТЬ
        self.end_music.setLoopCount(1)

        #СМОТРИМ СУЩЕСТВУЕТ ЛИ ФАЙЛ settings.json
        if len(self.all_file_options) == 0:
            result = QtWidgets.QMessageBox.critical(self,'Файл настроек не найден или поврежден','Внимание файл настроек settings.json не найден или поврежден. Дальнейшая работа программы не возможна!',buttons = QtWidgets.QMessageBox.Ok)
            if result == 1024:
                sys.exit()

        vertical_box_all = QtWidgets.QVBoxLayout()
        #HEADER
        header = QtWidgets.QLabel()
        header.setPixmap(QtGui.QPixmap((os.path.join('.','files','pic','header.png'))))
        #РАСТЯЖЕНИЕ КАРТИНКИ
        header.setScaledContents(True)
        header.setAlignment(QtCore.Qt.AlignCenter)
        header.setFixedHeight(100)
        vertical_box_all.addWidget(header)
        #CHANGE FILES
        gorizont_box_3 = QtWidgets.QHBoxLayout()
        vertical_box_all.addLayout(gorizont_box_3)
        
        group_box_3 = QtWidgets.QGroupBox('change folder: ')
        group_box_3.setToolTip('Выберите папку с файлом(ами) *.txt для редактирования')
        group_box_3.setFont(QtGui.QFont('Xpressive'))
        gorizont_box_3.addWidget(group_box_3)
        gorizont_box_5 = QtWidgets.QHBoxLayout()
        gorizont_box_5.setSpacing(1)
        group_box_3.setLayout(gorizont_box_5)
        self.change_files = QtWidgets.QLineEdit()
        self.change_files.setText(self.all_file_options['browse'])
        self.change_files.setReadOnly(True)
        self.change_files.setMaxLength(100)
        #ВЫБИРАЕМ ПАПКУ С ФАЙЛАМИ
        def path_folder_wih_files():
            dir_with_flies = QtWidgets.QFileDialog.getExistingDirectory(parent = self,directory = self.all_file_options['browse'])
            self.change_files.setText(dir_with_flies)
            #LCD ЗАДАЕМ ЗНАЧЕНИЕ
            lcd_search_files.display(len(files_on_folder(dir_with_flies)))
            #STATUSBAR ЗАДАЕМ ЗНАЧЕНИЕ
            progress.setRange(0,len(files_on_folder(dir_with_flies)))

            
        button_change = QtWidgets.QPushButton('browse')
        button_change.setFont(QtGui.QFont('Xpressive'))
        button_change.setIcon(QtGui.QIcon(os.path.join('.','files','pic','browse.png')))
        button_change.setStyleSheet('background-color: #b3ecec;')
        button_change.clicked.connect(path_folder_wih_files)
        gorizont_box_5.addWidget(button_change)
        gorizont_box_5.addWidget(self.change_files)
        #BACKUP OPTIONS
        group_box_6 = QtWidgets.QGroupBox('backup?')
        group_box_6.setFont(QtGui.QFont('Xpressive'))
        group_box_6.setToolTip('Делать ли резервные копии файлов, до редактирования')
        gorizont_box_3.addWidget(group_box_6)
        gorizont_box_7 = QtWidgets.QHBoxLayout()
        gorizont_box_7.setSpacing(1)
        group_box_6.setLayout(gorizont_box_7)
        radio_button_1 = QtWidgets.QRadioButton('yes')
        radio_button_1.setStyleSheet('color: green;')
        radio_button_1.setFont(QtGui.QFont('Xpressive'))
        radio_button_2 = QtWidgets.QRadioButton('no')
        radio_button_2.setStyleSheet('color: red;')
        radio_button_2.setFont(QtGui.QFont('Xpressive'))
        radio_button_2.setChecked(True)
        gorizont_box_7.addWidget(radio_button_1)
        gorizont_box_7.addWidget(radio_button_2)
        
        
        #LCD КОЛИЧЕСТВО ФАЙЛОВ
        group_box_5 = QtWidgets.QGroupBox('found files: *.txt')
        group_box_5.setFont(QtGui.QFont('Xpressive'))
        group_box_5.setToolTip('Найдено файлов с разрешением *.txt, в выбранной папке')
        gorizont_box_3.addWidget(group_box_5)
        gorizont_box_6 = QtWidgets.QHBoxLayout()
        gorizont_box_6.setSpacing(1)
        group_box_5.setLayout(gorizont_box_6)
        lcd_search_files = QtWidgets.QLCDNumber(5)
        lcd_search_files.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        lcd_search_files.setStyleSheet('background-color: #16b7ec; color : #1e5c89;')
        
        lcd_search_files.display(len(files_on_folder(self.change_files.text())))
        gorizont_box_6.addWidget(lcd_search_files)
        
        
        vkladki = QtWidgets.QTabWidget()
        #ONE PAGE
        two_tables = Body_Table()
        vkladki.addTab(two_tables,'TYPE FILE: txt')
        vkladki.setToolTip('Редактирование файлов только в формате txt')
        vkladki.setFont(QtGui.QFont('pollock2ctt'))
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
        button_start.setFont(QtGui.QFont("You're Gone"))
        button_start.setToolTip('Запуск процесса редактирования файлов')
        button_test = QtWidgets.QPushButton('Test')
        button_test.setStyleSheet('background-color: #b9f58a')
        button_test.setToolTip('Просмотр результата редактирования файлов, на примере одного файла (сам файл не изменяется)')
        button_test.setFont(QtGui.QFont("You're Gone"))
        
        #МЕНЯЕМ ЦВЕТ И ТЕКСТ КНОПКИ
        def eff_dutton_test_on():
            button_test.setText('Wait')
            button_test.setStyleSheet('background-color: red')
           
        button_test.pressed.connect(eff_dutton_test_on)
        
        #МЕНЯЕМ ЦВЕТ И ТЕКСТ КНОПКИ
        def eff_dutton_test_off():
            button_test.setText('Test')
            button_test.setStyleSheet('background-color: #e9e9e9')

        button_test.released.connect(eff_dutton_test_off)
        
        button_test.setIcon(QtGui.QIcon(os.path.join('.','files','pic','test.png')))
        button_start.setStyleSheet('background-color: green')
        button_start.setIcon(QtGui.QIcon(os.path.join('.','files','pic','start.png')))
        button_stop = QtWidgets.QPushButton('Stop')
        button_stop.setFont(QtGui.QFont("You're Gone"))
        button_stop.setStyleSheet('background-color: red')
        button_stop.setIcon(QtGui.QIcon(os.path.join('.','files','pic','close.png')))

        
        
        self.mythread = Mechanika()
        
        #СИГНАЛ ЧТО ФАЙЛОВ В ПАПКЕ НЕТ
        def not_files():
            self.change_files.setStyleSheet('background-color: red;')
            result = QtWidgets.QMessageBox.information(self,'Папка с файлами не выбрана или ...','Папка с файлами не выбрана или в текущей папке нет файлов txt',defaultButton = QtWidgets.QMessageBox.Ok)
            if result == 1024:
                self.change_files.setStyleSheet('background-color: #e9e9e9;')
    
    
        
        #КНОПКА СТАРТ
        def on_start():
            #ДЛЯ СТАРТА ПЕРИФЕРИЙНЫХ МОДУЛЕЙ
            Mechanika.stop_now = True
            #ЕСЛИ ФАЙЛОВ В ПАПКЕ НЕТ
            if lcd_search_files.value() == 0:
                not_files()
            else:
                #ПУТЬ ПАПКИ С ФАЙЛАМИ ДЛЯ ОБРАБОТКИ
                self.mythread.files_on_folder(self.change_files.text())
                #BACKUP STATUS
                self.mythread.backup_yes_or_no(radio_button_1.isChecked())
                #СПИСОК ФУНКЦИЙ ДЛЯ ОБРАБОТКИ ТЕКСТА
                list_func = two_tables.editors_list()
                self.mythread.funcs_to_mechanika(list_func)
                if not self.mythread.isRunning():
                    self.mythread.start()
                    gorizont_box_1.replaceWidget(button_start,button_stop)
                    button_start.setHidden(True)
                    button_log.setStyleSheet('background-color: #e5f389')
                    button_stop.setHidden(False)
                    group_box_3.setEnabled(False)
                    group_box_6.setEnabled(False)
                    group_box7.setEnabled(False)
                    vkladki.setEnabled(False)
        
        #ВОЗВРАЩАЕМ ЭЛЕМЕНТАМ КЛИКАБЕЛЬНОСТЬ
        def clickable_elm():
            button_start.setHidden(False)
            button_stop.setHidden(True)
            group_box_3.setEnabled(True)
            group_box_6.setEnabled(True)
            group_box7.setEnabled(True)
            vkladki.setEnabled(True)
            #ПРОИГРЫВАЕМ В КОНЦЕ ОБРАБОТКИ МУЗЫКУ
            if self.all_file_options.get('MUSIC') == 'On':
                self.end_music.play()
            
        #КНОПКА СТОП
        def on_stop():
            self.mythread.running = False
            #ДЛЯ ОСТАНОВКИ ПЕРИФЕРИЙНЫХ МОДУЛЕЙ
            Mechanika.stop_now = False
            gorizont_box_1.replaceWidget(button_stop,button_start)
            clickable_elm()
            
        
        #СТАТУС
        def on_change():
            gorizont_box_1.replaceWidget(button_stop,button_start)
            clickable_elm()
            #КРАСИМ КНОПКУ LOG
            for i in self.mythread.log:
                if i.endswith('[Error]</b>') == True:
                    button_log.setStyleSheet('background-color: red;')
                    break
            
            
            
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
        progress.setStyleSheet('background-color: #16b7ec; color : #1e5c89;')
        gorizont_box_2.addWidget(progress)
        progress.setRange(0,lcd_search_files.intValue())
        #HELP AND ABOUT
        group_box7 = QtWidgets.QGroupBox()
        gorizont_box.addWidget(group_box7)
        gorizont_box_10 = QtWidgets.QHBoxLayout()
        group_box7.setLayout(gorizont_box_10)
        button_log = QtWidgets.QPushButton('Log')
        button_log.setStyleSheet('background-color: #e5f389; color : black;')
        button_log.setToolTip('Посмотреть лог файл процесса редактирования файлов')
        button_log.setFont(QtGui.QFont("You're Gone"))
        button_log.setIcon(QtGui.QIcon(os.path.join('.','files','pic','log.png')))
        button_about = QtWidgets.QPushButton('About')
        button_about.setStyleSheet('background-color: #e5f389; color : black;')
        button_about.setToolTip('Настройка и описание программы')
        button_about.setFont(QtGui.QFont("You're Gone"))
        button_about.setIcon(QtGui.QIcon(os.path.join('.','files','pic','about.png')))
        button_close = QtWidgets.QPushButton('Close')
        button_close.setStyleSheet('background-color: #e81bbf; color : black;')
        button_close.setToolTip('Выход из программы')
        button_close.setFont(QtGui.QFont("You're Gone"))
        button_close.setIcon(QtGui.QIcon(os.path.join('.','files','pic','exit.png')))
        
        itslog = LogView()
        
        #ДЛЯ ОТОБРАЖЕНИЯ LOGa
        def log_view():
            itslog.add_log_info(self.mythread.log)
            itslog.show()
            
        button_log.clicked.connect(log_view)
        #ДЛЯ ОТОБРАЖЕНИЯ ABOUT
        def about_view():
            ABOUT = About(3)
            ABOUT.show()
            
        button_about.clicked.connect(about_view)
            
        button_close.clicked.connect(lambda: self.close())
        
        gorizont_box_10.addWidget(button_log)
        gorizont_box_10.addWidget(button_about)
        gorizont_box_10.addWidget(button_close)
        #ПУСТОЕ МЕСТО
        gorizont_box_footer = QtWidgets.QHBoxLayout()
        signature0 = QtWidgets.QLabel('autor and design: ')
        signature0.setFont(QtGui.QFont("Amazone BT"))
        signature = QtWidgets.QLabel()
        signature.setPixmap(QtGui.QPixmap(os.path.join('.','files','pic','min_sign.png')))
        gorizont_box_footer.addWidget(signature0,alignment = QtCore.Qt.AlignRight)
        gorizont_box_footer.addWidget(signature,alignment = QtCore.Qt.AlignLeft)
        vertical_box_all.addLayout(gorizont_box_footer)

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
        save_options(self.all_file_options)
        
        QtWidgets.QApplication.closeAllWindows()
        e.accept()
        
        


if __name__ == '__main__':
    app =  QtWidgets.QApplication(sys.argv)
    window = Body()
    window.show()
    sys.exit(app.exec_())
