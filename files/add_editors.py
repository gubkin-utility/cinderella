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
#разбить файл(ы) по количеству строк
#========================================================    
#ОКНО НАСТРОЙКИ РЕДАКТОРА ТЕКСТА
def split_files_view():
    from files.text_editors.split_files.view import View
    View()

#САМ РЕДАКТОР
def split_files_edit(list,i):
    from files.text_editors.split_files.editor import editor
    editor(list,i)
#========================================================
#удаленить пустоты в конце строки
#========================================================    
#ОКНО НАСТРОЙКИ РЕДАКТОРА ТЕКСТА
def right_strip_str_view():
    from files.text_editors.right_strip_str.view import View
    View()

#САМ РЕДАКТОР
def right_strip_str_edit(list):
    from files.text_editors.right_strip_str.editor import editor
    return editor(list)
#========================================================
#преобразовать строки текста - в верхний регистр
#========================================================    
#ОКНО НАСТРОЙКИ РЕДАКТОРА ТЕКСТА
def str_to_uppercase_view():
    from files.text_editors.str_to_uppercase.view import View
    View()

#САМ РЕДАКТОР
def str_to_uppercase_edit(list):
    from files.text_editors.str_to_uppercase.editor import editor
    return editor(list)
#========================================================
#преобразовать строки текста - в нижний регистр
#========================================================    
#ОКНО НАСТРОЙКИ РЕДАКТОРА ТЕКСТА
def str_to_lowercase_view():
    from files.text_editors.str_to_lowercase.view import View
    View()

#САМ РЕДАКТОР
def str_to_lowercase_edit(list):
    from files.text_editors.str_to_lowercase.editor import editor
    return editor(list)
#========================================================
#преобразовать строки текста - каждое слово с заглавной буквы
#========================================================    
#ОКНО НАСТРОЙКИ РЕДАКТОРА ТЕКСТА
def str_to_titlecase_view():
    from files.text_editors.str_to_titlecase.view import View
    View()

#САМ РЕДАКТОР
def str_to_titlecase_edit(list):
    from files.text_editors.str_to_titlecase.editor import editor
    return editor(list)
#========================================================
#удалить или заменить слова,строки,символы
#========================================================    
#ОКНО НАСТРОЙКИ РЕДАКТОРА ТЕКСТА
def remove_str_view():
    from files.text_editors.remove_str.view import View
    View()

#САМ РЕДАКТОР
def remove_str_edit(list):
    from files.text_editors.remove_str.editor import editor
    return editor(list)
#========================================================
#удалить или заменить слова,строки,символы
#========================================================    
#ОКНО НАСТРОЙКИ РЕДАКТОРА ТЕКСТА
def join_files_view():
    from files.text_editors.join_files.view import View
    View()

#САМ РЕДАКТОР
def join_files_edit(list,i):
    from files.text_editors.join_files.editor import editor
    return editor(list,i)
#========================================================
#удалить одинаковые предложения
#========================================================    
#ОКНО НАСТРОЙКИ РЕДАКТОРА ТЕКСТА
def delete_duplicate_str_view():
    from files.text_editors.delete_duplicate_str.view import View
    View()

#САМ РЕДАКТОР
def delete_duplicate_str_edit(list):
    from files.text_editors.delete_duplicate_str.editor import editor
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
    'удалить пустоты в начале строки':[left_strip_str_view,left_strip_str_edit,False,],
    'разбить файл(ы) по количеству строк':[split_files_view,split_files_edit,True,],
    'удалить пустоты в конце строки':[right_strip_str_view,right_strip_str_edit,False,],
    'преобразовать строки текста - в верхний регистр':[str_to_uppercase_view,str_to_uppercase_edit,False,],
    'преобразовать строки текста - в нижний регистр':[str_to_lowercase_view,str_to_lowercase_edit,False,],
    'преобразовать строки текста - каждое слово с заглавной буквы':[str_to_titlecase_view,str_to_titlecase_edit,False,],
    'удалить или заменить слова,строки,символы':[remove_str_view,remove_str_edit,True,],
    'объединить, склеить файлы в один файл':[join_files_view,join_files_edit,False,],
    'удалить одинаковые строки':
[delete_duplicate_str_view,delete_duplicate_str_edit,False,],
    
    }
