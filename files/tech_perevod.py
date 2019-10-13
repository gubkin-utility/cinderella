#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on  05.09.2019

@author: Gubkin Leonid

Cinderella - Text Editor

"""

from files.about import About

About

dd = About.about_options['LAGUANGE']

if dd == 'English':
    lang = 0
else:
    lang = 1
print(dd)


trans1 = ['Делать ли резервные копии файлов, до редактирования','x'][lang]