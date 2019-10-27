#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on  05.09.2019

@author: Gubkin Leonid

Cinderella - Text Editor

"""


from PyQt5 import QtWidgets, QtGui, QtCore
from files.text_editors.techfunction import tocenter,title_project,icon_project,upload_options,save_options
import sys, os

#=============================================================
#ABOUT
#=============================================================

class About(QtWidgets.QWidget):
    def __init__(self,set_akkardion_ind,parent=None):
        QtWidgets.QFrame.__init__(self,parent)
        self.setWindowIcon(QtGui.QIcon(icon_project))
        self.setWindowTitle(title_project + ' | About')
        self.setWindowFlags(QtCore.Qt.Window|QtCore.Qt.FramelessWindowHint)
        self.setWindowFlags(QtCore.Qt.Window|QtCore.Qt.WindowStaysOnTopHint|QtCore.Qt.MSWindowsFixedSizeDialogHint)
        self.resize(500,390)
#        self.setStyleSheet('background-color: #e9e9e9; color : black;')
        self.setStyleSheet("""
                           QToolTip { 
                           background-color: yellow; 
                           color: black; 
                           border: black solid 1px}
                           QWidget::title{
                           font-family: Cousine;}
                           QWidget{ 
                           background-color: #bae1ff;
                           color : black;}  
                           QRadioButton{ 
                           background-color: #bae1ff;
                           color : black;
                           font-family: pollock2ctt;}
                           QLabel{ 
                           background-color: #bae1ff;
                           color : navy;
                           font-family: pollock2ctt;}
                           """)
        #ПО ЦЕНТРУ
        tocenter(self)
        self.akkardion = QtWidgets.QToolBox()
        self.akkardion.setFont(QtGui.QFont("You're Gone"))
        
        #НАСТРОЙКИ ИЗ JSON
        about_options = upload_options()
        #НАСТРОЙКИ ЯЗЫКА
        def save_laguange():    
            try:
                if rbutton_eng.isChecked() == True:
                    laguange = rbutton_eng.text()
                else: 
                    laguange = rbutton_rus.text()
                #СОХР. 
                about_options['LAGUANGE'] = laguange
                save_options(about_options)
                button_ok.setStyleSheet('background-color: green;')
                
            except:
                QtWidgets.QMessageBox.critical(self,'Настройки не сохранены!','Возможно файл настроек settings.json не найден или поврежден. Дальнейшая работа программы не возможна!', defaultButton = QtWidgets.QMessageBox.Ok)
            
            
        
        
        change_laguange = QtWidgets.QWidget()
        vertical_box_00 = QtWidgets.QVBoxLayout()
        rbutton_rus = QtWidgets.QRadioButton('Russian')
        rbutton_rus.setStyleSheet('background-color: #bae1ff; color : black;')
        rbutton_rus.setFont(QtGui.QFont('pollock2ctt'))
        rbutton_eng = QtWidgets.QRadioButton('English')
        rbutton_eng.setEnabled(False)
        rbutton_eng.setStyleSheet('background-color: #bae1ff; color : black;')
        rbutton_eng.setFont(QtGui.QFont('pollock2ctt'))
        button_ok = QtWidgets.QPushButton()
        button_ok.setIcon(QtGui.QIcon(os.path.join('.','files','pic','ok.png')))
        if about_options['LAGUANGE'] == 'English':
            rbutton_eng.setChecked(True)
        else:
            rbutton_rus.setChecked(True)
           
        rbutton_rus.toggled.connect(lambda:button_ok.setStyleSheet('background-color: #bae1ff;'))
        rbutton_eng.toggled.connect(lambda:button_ok.setStyleSheet('background-color: #bae1ff;'))
        button_ok.setStyleSheet('background-color: #b3ecec; color : black;')
        
        self.inform_text0 = QtWidgets.QLabel()
        self.inform_text0.setText('* Настройки всупят в силу после перезагрузки программы!')
        
        vertical_box_00.addWidget(rbutton_rus)
        vertical_box_00.addWidget(rbutton_eng)
        vertical_box_00.addWidget(button_ok,alignment = QtCore.Qt.AlignRight)
        vertical_box_00.addSpacing(89)
        vertical_box_00.addWidget(self.inform_text0,alignment = QtCore.Qt.AlignBottom|QtCore.Qt.AlignCenter)
        change_laguange.setLayout(vertical_box_00)
        change_laguange.setSizePolicy(QtWidgets.QSizePolicy.Minimum,QtWidgets.QSizePolicy.Maximum)
        button_ok.setSizePolicy(QtWidgets.QSizePolicy.Maximum,QtWidgets.QSizePolicy.Maximum)
        button_ok.clicked.connect(save_laguange)
        self.akkardion.addItem(change_laguange,'Language setting')
        
        #НАСТРОЙКИ ЗВУКА
        def save_music():
            try:
                if self.rbutton_music_on.isChecked() == True:
                    music = self.rbutton_music_on.text()
                else: 
                    music = self.rbutton_music_off.text()
                #СОХР. 
                about_options['MUSIC'] = music
                save_options(about_options)
                button_ok2.setStyleSheet('background-color: green;')
                
            except:
                QtWidgets.QMessageBox.critical(self,'Настройки не сохранены!','Возможно файл настроек settings.json не найден или поврежден. Дальнейшая работа программы не возможна!', defaultButton = QtWidgets.QMessageBox.Ok)
            
                  
        
        change_music = QtWidgets.QWidget()
        vertical_box_000 = QtWidgets.QVBoxLayout()
        self.rbutton_music_on = QtWidgets.QRadioButton('On')
        self.rbutton_music_on.setStyleSheet('color: green;')
        self.rbutton_music_off = QtWidgets.QRadioButton('Off')
        self.rbutton_music_off.setStyleSheet('color: red;')
        button_ok2 = QtWidgets.QPushButton()
        button_ok2.setIcon(QtGui.QIcon(os.path.join('.','files','pic','ok.png')))
        self.rbutton_music_on.toggled.connect(lambda:button_ok2.setStyleSheet('background-color: #bae1ff;'))
        self.rbutton_music_off.toggled.connect(lambda:button_ok2.setStyleSheet('background-color: #bae1ff;'))
        
        if about_options['MUSIC'] == 'On':
            self.rbutton_music_on.setChecked(True)
        else:
            self.rbutton_music_off.setChecked(True)
            
        self.inform_text = QtWidgets.QLabel()
        self.inform_text.setText('* Настройки всупят в силу после перезагрузки программы!')
        vertical_box_000.addWidget(self.rbutton_music_on)
        vertical_box_000.addWidget(self.rbutton_music_off)
        vertical_box_000.addWidget(button_ok2,alignment = QtCore.Qt.AlignRight)
        vertical_box_000.addSpacing(89)
        vertical_box_000.addWidget(self.inform_text,alignment = QtCore.Qt.AlignBottom|QtCore.Qt.AlignCenter)
        
        change_music.setLayout(vertical_box_000)
        change_music.setSizePolicy(QtWidgets.QSizePolicy.Minimum,QtWidgets.QSizePolicy.Maximum)
        button_ok2.setSizePolicy(QtWidgets.QSizePolicy.Maximum,QtWidgets.QSizePolicy.Maximum)
        button_ok2.clicked.connect(save_music)
        self.akkardion.addItem(change_music,'Sound Setting')        
        
        #ПОЖЕРТВОВАНИЕ
        spasibo_text = '<p></p>'
        spacibo = QtWidgets.QTextEdit(spasibo_text)
        spacibo.setFont(QtGui.QFont("Cousine"))
        spacibo.setReadOnly(True)
        self.akkardion.addItem(spacibo,'Donation')
        
        #О ПРОГРАММЕ
        about_text = '''
        <p><u> name:</u> <b>Cinderella</b></p>
        <p><u>description:</u> Micro text editor</p>
        <p><u>license:</u> Apache 2.0 </p>
        <p><u>author:</u> <a href="https://www.facebook.com/leonid.gubkin">https://www.facebook.com/leonid.gubkin</a></p>
        <p><u>site:</u> <a href="http://github.com/">github.com</a></p>
        <p><u>youtube:</u> <a href="http://youtube.com/">youtube.com</a></p>       
        '''
        abouts = QtWidgets.QTextEdit(about_text)
        abouts.setFont(QtGui.QFont("Cousine"))
        abouts.setTextInteractionFlags(QtCore.Qt.TextBrowserInteraction)
        abouts.setStyleSheet('background: url(files/pic/trademark.png) no-repeat; color : black;')

        self.akkardion.addItem(abouts,'About')
        self.akkardion.setCurrentIndex(set_akkardion_ind)
        vertical_box = QtWidgets.QVBoxLayout()
        vertical_box.addWidget(self.akkardion)
        self.setLayout(vertical_box)
        
        button_exit = QtWidgets.QPushButton('Close')
        button_exit.setFont(QtGui.QFont("You're Gone"))
        button_exit.setStyleSheet("background-color: #fcaecd;")
        button_exit.setIcon(QtGui.QIcon(os.path.join('.','files','pic','close.png')))
        

        button_exit.clicked.connect(lambda:self.close())        
        vertical_box.addWidget(button_exit,alignment = QtCore.Qt.AlignCenter)
        
        

if __name__ == '__main__':
    app =  QtWidgets.QApplication(sys.argv)
    window = About(0)
#    options = Options()
    window.show()
    sys.exit(app.exec_())
