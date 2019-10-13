#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on  05.09.2019

@author: Gubkin Leonid

Cinderella - Text Editor

"""
#========================================================
#Перемешивание строк текста
#========================================================
#ОКНО РЕДАКТОРА
def random_lines_view():
    from files.text_editors.random_lines.view import View
    View()

#РЕДАКТОР
def random_lines_edit(list):
    from files.text_editors.random_lines.editor import editor
    return editor(list)
#========================================================    
#Сортировка текста по длинне
#========================================================    
#ОКНО НАСТРОЙКИ РЕДАКТОРА ТЕКСТА
def sort_len_view():
    from files.text_editors.sort_len.view import View
    View()

#САМ РЕДАКТОР
def sort_len_edit(list):
    from files.text_editors.sort_len.editor import editor
    return editor(list)
#========================================================    
#удалить пустые строки
#========================================================    
#ОКНО НАСТРОЙКИ РЕДАКТОРА ТЕКСТА
def delete_null_str_view():
    from files.text_editors.delete_null_str.view import View
    View()

#САМ РЕДАКТОР
def delete_null_str_edit(list):
    from files.text_editors.delete_null_str.editor import editor
    return editor(list)
#========================================================    
#удалить строки текста по длинне
#========================================================    
#ОКНО НАСТРОЙКИ РЕДАКТОРА ТЕКСТА
def delete_str_len_view():
    from files.text_editors.delete_str_len.view import View
    View()

#САМ РЕДАКТОР
def delete_str_len_edit(list):
    from files.text_editors.delete_str_len.editor import editor
    return editor(list)
#======================================================== 
#удаленить пустоты в начале строки
#========================================================    
#ОКНО НАСТРОЙКИ РЕДАКТОРА ТЕКСТА
def left_strip_str_view():
    from files.text_editors.left_strip_str.view import View
    View()

#САМ РЕДАКТОР
def left_strip_str_edit(list):
    from files.text_editors.left_strip_str.editor import editor
    return editor(list)
#======================================================== 


#1.ОКНО НАСТРОЙКИ РЕДАКТОРА ТЕКСТА
#2.САМ РЕДАКТОР
#3.True ЕСЛИ НАСТРОЙКИ РЕДАКТОРА, ИНАЧЕ False
all_editors = {
    'удалить пустые строки':[delete_null_str_view,delete_null_str_edit,False,],
    'сортировать строки по длинне':[sort_len_view,sort_len_edit,True,],
    'перемешать строки текста':[random_lines_view,random_lines_edit,False,],
    'удалить строки текста по длинне':[delete_str_len_view,delete_str_len_edit,True,],
    'удаленить пустоты в начале строки':[left_strip_str_view,left_strip_str_edit,True,],
    
    }


