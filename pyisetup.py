import sys
from cx_Freeze import setup, Executable

includes = ["PyQt5.QtCore","PyQt5.QtGui","re",]

base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup(  name = "x6",
        version = "0.0.1",
        options = {"build_exe": {"includes": includes}},
        executables = [Executable('MainWindow.py', base=base, targetName='x6.exe',compress=True, icon="x6.ico")])