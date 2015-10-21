#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from cx_Freeze import setup, Executable
import collections
import os
from glob import glob
import PyQt5
from PyQt5 import QtGui, QtCore
from PyQt5.QtCore import pyqtSlot, Qt, QFileInfo, QRegExp
from PyQt5.QtGui import (QClipboard, QFont, QFontDatabase, QFontMetrics,
        QPainter)
from PyQt5.QtWidgets import (QDialog, QAbstractItemView, QAction, QActionGroup,
        QApplication, QComboBox, QFileDialog, QFrame, QGridLayout, QGroupBox,
        QHBoxLayout, QHeaderView, QItemDelegate, QLabel, QMainWindow,
        QMessageBox, QRadioButton, QSizePolicy, QSpinBox, QStyle,
        QStyleFactory, QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget,  QLineEdit, QPushButton)

base = None

if sys.platform == 'win32':
    base = 'Win32GUI'

'''
build_exe_options = {
"includes": ['sys', 'PyQt5', 'PyQt5.Core', 'PyQt5.QtGui', 'PyQt5.QtWidgets', 'os', 'os.path', 'ftplib',
    'traceback', 'time',],
"packages": ["os", "sys", "collections", "datetime", "pandas", "numpy", "glob", "itertools",'PyQt5'],
"excludes": ["PyQt5"],
"include_files" : ['number.dat','number2.dat',"x6.ico", (r'C:\Windows\System32\msvcr100.dll', 'msvcr100.dll'),
                   (r'C:\Python34\Lib\site-packages\PyQt5\libEGL.dll', 'libEGL.dll')],
#'dll_includes': ['msvcr100.dll'],
'include_msvcr' : True,
}

build_exe_options = dict(
includes = ['numpy', 'pandas'],
packages = ["os", "sys", "collections", "datetime", "pandas", "numpy", "glob", "itertools"], excludes = [],
include_files = ['number.csv', 'number2.csv',"x6.ico", (r'C:\Windows\System32\msvcr100.dll', 'msvcr100.dll'),],
)
'''
build_exe_options = dict(
includes = ['atexit'],
packages = [], excludes = [],
include_files = ['number.csv', 'number2.csv',"vague.ico", (r'C:\Windows\System32\msvcr100.dll', 'msvcr100.dll'),
                 (r'C:\Python34\Lib\site-packages\PyQt5\libEGL.dll', 'libEGL.dll'),
                 (r'C:\Windows\System32\msvcp100.dll', 'msvcp100.dll'),
                 (r'C:\Python34\Lib\site-packages\PyQt5\libGLESv2.dll', 'libGLESv2.dll'),],
)


#executables = [Executable('MainWindow.py', base=base, targetName='x6.exe',compress=True, icon="x6.ico", shortcutName="X6", shortcutDir="DesktopFolder")]
executables = [Executable('MainWindow.py', base=base, targetName='Vogue.exe', icon="vague.ico",compress=True, shortcutName="Vogue", shortcutDir="DesktopFolder")]

setup(
    name="Vogue",
    version="1.0.0",
    author='chenyr',
    author_email='chenyeren77@163.com',
    description="lottery anasisy",
    options={"build_exe": build_exe_options},
    executables=executables,
)
