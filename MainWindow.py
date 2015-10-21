#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
from collections import Counter
from PyQt5.QtGui import QColor
import pandas as pd
import numpy as np

from PyQt5 import QtGui, QtCore
from PyQt5.QtCore import pyqtSlot, Qt, QFileInfo, QRegExp
from PyQt5.QtGui import (QClipboard, QFont, QFontDatabase, QFontMetrics,
        QPainter)
from PyQt5.QtWidgets import (QDialog, QAbstractItemView, QAction, QActionGroup,
        QApplication, QComboBox, QFileDialog, QFrame, QGridLayout, QGroupBox,
        QHBoxLayout, QHeaderView, QItemDelegate, QLabel, QMainWindow,
        QMessageBox, QRadioButton, QSizePolicy, QSpinBox, QStyle,
        QStyleFactory, QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget,  QLineEdit, QPushButton)

from Ui_MainWindow import Ui_MainWindow
import interface
import common
from datetime import datetime
from pandas.core.frame import DataFrame

class Login(QDialog):
    def __init__(self, parent=None):
        super(Login, self).__init__(parent)
        usr = QLabel(u"用户：")
        pwd = QLabel(u"密码：")
        self.usrLineEdit = QLineEdit()
        self.pwdLineEdit = QLineEdit()
        self.pwdLineEdit.setEchoMode(QLineEdit.Password)

        gridLayout = QGridLayout()
        gridLayout.addWidget(usr, 0, 0, 1, 1)
        gridLayout.addWidget(pwd, 1, 0, 1, 1)
        gridLayout.addWidget(self.usrLineEdit, 0, 1, 1, 3);
        gridLayout.addWidget(self.pwdLineEdit, 1, 1, 1, 3);

        okBtn = QPushButton(u"确定")
        cancelBtn = QPushButton(u"取消")
        btnLayout = QHBoxLayout()

        btnLayout.setSpacing(60)
        btnLayout.addWidget(okBtn)
        btnLayout.addWidget(cancelBtn)

        dlgLayout = QVBoxLayout()
        dlgLayout.setContentsMargins(40, 40, 40, 40)
        dlgLayout.addLayout(gridLayout)
        dlgLayout.addStretch(40)
        dlgLayout.addLayout(btnLayout)

        self.setLayout(dlgLayout)
        okBtn.clicked.connect(self.accept)
        cancelBtn.clicked.connect(self.reject)
        self.setWindowTitle(u"登录")
        self.resize(300, 200)

    def accept(self):
        #year = strftime("%Y",localtime())
        dt = datetime.now()
        if self.usrLineEdit.text().strip() == "kerun" and self.pwdLineEdit.text() == "188102377":
            super(Login, self).accept()
        else:
            QMessageBox.warning(self,
                    u"警告",
                    u"用户名或密码错误！",
                    QMessageBox.Yes)
            self.usrLineEdit.setFocus()

class TabThread(QtCore.QThread):
    trigger = QtCore.pyqtSignal(str)

    def __init__(self, parent=None):
        super(TabThread, self).__init__(parent)
        self.window = parent

    def run(self):
        starttime = datetime.now()
        activeTab = self.window.getActiveTab()
        if activeTab == 2:
            cond = {}
            cond['num1'] = self.window.t2_qian_sb.text()
            cond['num2'] = self.window.t2_bai_sb.text()
            cond['num3'] = self.window.t2_shi_sb.text()
            cond['num4'] = self.window.t2_ge_sb.text()
            cond['error'] = self.window.t2_err_sb.text()
            cond['h2err'] = self.window.t2_h2err_sb.text()
            cond['h3err'] = self.window.t2_h2err_sb.text()

            filePath = self.window.filePathLe.text() + '\\' + u'第一步'

            if not os.path.exists(filePath):
                os.mkdir(filePath)

            interface.first(cond,filePath, self)
            self.window.t2_execute_btn.setEnabled(True)
        elif activeTab == 3:
            cond = {}
            cond['ab'] = self.window.t3_ab_sb.text()
            cond['ac'] = self.window.t3_ac_sb.text()
            cond['ad'] = self.window.t3_ad_sb.text()
            cond['bc'] = self.window.t3_bc_sb.text()
            cond['bd'] = self.window.t3_bd_sb.text()
            cond['cd'] = self.window.t3_cd_sb.text()
            cond['error'] = self.window.t3_err_sb.text()
            cond['h2err'] = self.window.t3_h2err_sb.text()
            cond['h3err'] = self.window.t3_h3err_sb.text()

            filePath = self.window.filePathLe.text() + '\\' + u'第二步'

            if not os.path.exists(filePath):
                os.mkdir(filePath)

            interface.second(cond,filePath, self)
            self.window.t3_execute_btn.setEnabled(True)
        elif activeTab == 6:
            cond = {}
            cond['num1'] = self.window.t6_qian_sb.text()
            cond['num2'] = self.window.t6_bai_sb.text()
            cond['num3'] = self.window.t6_shi_sb.text()
            cond['num4'] = self.window.t6_ge_sb.text()
            cond['ab'] = str((int(cond['num1']) + int(cond['num2']))%10)
            cond['ac'] = str((int(cond['num1']) + int(cond['num3']))%10)
            cond['ad'] = str((int(cond['num1']) + int(cond['num4']))%10)
            cond['bc'] = str((int(cond['num2']) + int(cond['num3']))%10)
            cond['bd'] = str((int(cond['num2']) + int(cond['num4']))%10)
            cond['cd'] = str((int(cond['num3']) + int(cond['num4']))%10)
            cond['abc'] = str((int(cond['num1']) + int(cond['num2']) + int(cond['num3']))%10)
            cond['abd'] = str((int(cond['num1']) + int(cond['num2']) + int(cond['num4']))%10)
            cond['acd'] = str((int(cond['num1']) + int(cond['num3']) + int(cond['num4']))%10)
            cond['bcd'] = str((int(cond['num2']) + int(cond['num3']) + int(cond['num4']))%10)
            cond['checknum'] = self.window.t6_chknum_le.text()

            number = str(cond['num1']) + str(cond['num2']) + str(cond['num3']) + str(cond['num4'])

            filePath = self.window.filePathLe.text() + '\\' + number

            if not os.path.exists(filePath):
                os.mkdir(filePath)

            interface.oneKey(cond,filePath, self)
            self.window.t6_execute_btn.setEnabled(True)

        endtime = datetime.now()
        tend = endtime - starttime
        self.trigger.emit(u'执行时间：'+str(tend.seconds)+'秒')


class MainWindow(QMainWindow, Ui_MainWindow):

    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        self.threads = []
        self.activeTab = 6
        self.fileDicts = {}
        self.clipboard = QApplication.clipboard()

        # 分布变量
        self.nStart = 0
        self.nPageSize = 100
        self.nCurPageSize = 0
        self.nTotal = 0

        self.tabWidget.removeTab(1)
        self.tabWidget.removeTab(1)
        self.tabWidget.removeTab(1)
        self.tabWidget.removeTab(1)

        self.fileView.verticalHeader().setDefaultSectionSize(20)
        self.fileView.horizontalHeader().setDefaultSectionSize(50)
        self.fileView.setColumnCount(6)
        self.fileView.horizontalHeader().setSectionResizeMode(QHeaderView.Fixed)
        self.fileView.setHorizontalHeaderLabels((u"号码文件", u"组数", u"结果", u"序号",u"",u'原始序号'))
        #self.fileView.horizontalHeader().setSectionResizeMode(0, QHeaderView.Stretch)
        self.fileView.horizontalHeader().resizeSection(0,220)
        self.fileView.horizontalHeader().setSectionResizeMode(1, QHeaderView.Fixed)
        self.fileView.horizontalHeader().setSectionResizeMode(2, QHeaderView.Fixed)
        self.fileView.horizontalHeader().setSectionResizeMode(3, QHeaderView.Fixed)
        self.fileView.horizontalHeader().setSectionResizeMode(4, QHeaderView.Fixed)
        self.fileView.horizontalHeader().setSectionHidden(4, True)
        self.fileView.horizontalHeader().setSectionResizeMode(5, QHeaderView.Fixed)
        self.fileView.horizontalHeader().setSectionHidden(5, True)
        self.fileView.verticalHeader().hide()
        self.fileView.setAlternatingRowColors(True)

        self.highlighter = MyHighlighter(self.previewpte.document())

    def getActiveTab(self):
        return self.activeTab

    def logMessage(self, message):
        if self.activeTab == 2:
            self.t2_log_pte.append(message)
        elif self.activeTab == 3:
            self.t3_log_pte.append(message)
        elif self.activeTab == 4:
            self.t4_log_pte.append(message)
        elif self.activeTab == 5:
            self.t5_log_pte.append(message)
        elif self.activeTab == 6:
            self.t6_log_pte.append(message)

    def closeEvent(self, event):
        while self.threads:
            thread = self.threads[0]
            thread.terminate()
            thread.wait()
            self.threads.remove(thread)
            print('进程退出!')

    @pyqtSlot()
    def on_addBtn_clicked(self):
        fileNames, _ = QFileDialog.getOpenFileNames(self, "Open Files", '',
                "Files (*.txt);;All Files (*)")
        #self.fileDicts.clear()
        #self.fileView.setRowCount(0)
        #fileNames.sort()
        row = len(self.fileDicts)
        for fileName in fileNames:
            txtName = QFileInfo(fileName).baseName()
            with open(fileName, 'r') as f :
                content = f.read()
            contents = []
            contents = content.split(" ")
            fileDict = {}
            fileDict['content'] = content
            fileDict['filename'] = txtName
            fileDict['group'] = txtName[0:-2]
            fileDict['count'] = len(contents)
            fileDict['seq'] = str(row)
            self.fileDicts['seq_' + str(row).zfill(4)] = fileDict
            row += 1
        #self.nTotal = row
        self.updateFileDict()
        self.nStart = 0
        self.nextBtn.setEnabled(True)
        self.preBtn.setEnabled(False)
        self.updateTableUi()

    @pyqtSlot()
    def on_checkAllBtn_clicked(self):
        row = self.fileView.rowCount()
        for i in range(row):
            item = self.fileView.item(i,  3)
            item.setCheckState(Qt.Checked)

    @pyqtSlot()
    def on_clearAllBtn_clicked(self):
        row = self.fileView.rowCount()
        for i in range(row):
            item = self.fileView.item(i,  3)
            item.setCheckState(Qt.Unchecked)

    @pyqtSlot()
    def on_removeBtn_clicked(self):
        #self.fileView.setRowCount(0)
        #self.fileDicts.clear()
        row = self.fileView.rowCount()
        for i in range(row):
            item5 = self.fileView.item(i,  5)
            item3 = self.fileView.item(i,  3)
            if item3.checkState() == Qt.Checked :
                del self.fileDicts['seq_'+item5.text().zfill(4)]

        self.updateFileDict()
        self.nStart = 0
        self.nextBtn.setEnabled(True)
        self.preBtn.setEnabled(False)
        self.updateTableUi()

    @pyqtSlot()
    def on_allRemoveBtn_clicked(self):
        self.fileView.setRowCount(0)
        self.fileDicts.clear()
        self.nStart = 0
        self.nextBtn.setEnabled(False)
        self.preBtn.setEnabled(False)

    def updateFileDict(self):
        row = 0
        tempDict = {}
        for k in sorted(self.fileDicts.keys()):
            fileDict = {}
            fileDict['content'] = self.fileDicts[k]['content']
            fileDict['filename'] = self.fileDicts[k]['filename']
            fileDict['group'] = self.fileDicts[k]['group']
            fileDict['count'] = self.fileDicts[k]['count']
            #fileDict['seq'] = self.fileDicts[k]['seq']
            fileDict['seq'] = str(row).zfill(4)
            tempDict['seq_' + str(row).zfill(4)] =fileDict
            row += 1

        self.fileDicts.clear()
        self.fileDicts = tempDict
        self.nTotal = len(self.fileDicts)

    @pyqtSlot()
    def on_uncheckBtn_clicked(self):
        row = self.fileView.rowCount()
        for i in range(row):
            item = self.fileView.item(i,  3)
            if item.checkState() == Qt.Unchecked :
                 item.setCheckState(Qt.Checked)
            else :
                item.setCheckState(Qt.Unchecked)

    @pyqtSlot()
    def on_nextBtn_clicked(self):
        #self.fileView.setRowCount(0)
        self.nStart = self.nStart+self.nPageSize

        self.updateTableUi()
        self.preBtn.setEnabled(True)

    @pyqtSlot()
    def on_preBtn_clicked(self):
        #self.fileView.setRowCount(0)
        self.nStart = self.nStart-self.nPageSize if self.nStart-self.nPageSize > 0 else 0

        self.updateTableUi()
        self.nextBtn.setEnabled(True)
        if self.nStart == 0:
            self.preBtn.setEnabled(False)

    @pyqtSlot(int)
    def on_pagesizeSb_valueChanged(self, p0):
        pagesize = self.pagesizeSb.text()
        self.nPageSize = int(pagesize)
        self.nStart = 0
        self.nextBtn.setEnabled(True)
        self.preBtn.setEnabled(False)

        self.updateTableUi()

    def updateTableUi(self):
        self.fileView.setRowCount(0)
        end = self.nStart+self.nPageSize if self.nStart+self.nPageSize < self.nTotal else self.nTotal
        if end ==  self.nTotal:
            self.nextBtn.setEnabled(False)
        for i in range(self.nStart, end):
            subDict = self.fileDicts['seq_'+str(i).zfill(4)]

            row = self.fileView.rowCount()

            self.fileView.setRowCount(row + 1)
            item0 = QTableWidgetItem(subDict['filename'])
            if (row+1) % 10 == 0:
                textFont = QFont("Arial", 9, QFont.Bold)
                item0.setFont(textFont)
                item0.setForeground(QColor(255,0,0))

            item1 = QTableWidgetItem(str(subDict['count']))
            #√
            item2 = QTableWidgetItem('×')
            item2.setForeground(QColor(0,0,0))
            item2.setTextAlignment(Qt.AlignCenter)
            item3 = QTableWidgetItem(str(row + 1))
            item4 = QTableWidgetItem(subDict['content'])
            item5 = QTableWidgetItem(subDict['seq'])

            self.fileView.setItem(row, 0, item0)
            self.fileView.setItem(row, 1, item1)
            self.fileView.setItem(row, 2, item2)
            self.fileView.setItem(row, 3, item3)
            self.fileView.setItem(row, 4, item4)
            self.fileView.setItem(row, 5, item5)

            item3.setCheckState(Qt.Unchecked)

    @pyqtSlot()
    def on_intersetBtn_clicked(self):
        row = self.fileView.rowCount()
        resultList = []
        selcount = 0
        for i in range(row):
            item4 = self.fileView.item(i,  4)
            item3 = self.fileView.item(i,  3)
            if item3.checkState() == Qt.Checked:
                resultList += item4.text().split(' ')
                selcount += 1

        countlist = Counter(resultList)
        countlist = countlist.most_common()
        filterList = [str(tup[0]) for tup in countlist if int(tup[1]) == selcount]

        resultstr = ' '.join(filterList)
        self.previewpte.setPlainText(resultstr)
        self.resultLb.setText(str(len(filterList)) + u'组数据')

        checknum = self.checkNum.text()
        if checknum != '':
            self.highlighter.setHighlightData([checknum])
            self.highlighter.rehighlight()

    @pyqtSlot()
    def on_selectBtn_clicked(self):
        row = self.fileView.rowCount()
        err = self.selectErrSb.text()
        resultList = []
        selcount = 0
        for i in range(row):
            item4 = self.fileView.item(i,  4)
            item3 = self.fileView.item(i,  3)
            if item3.checkState() == Qt.Checked:
                resultList += item4.text().split(' ')
                selcount += 1

        countlist = Counter(resultList)
        countlist = countlist.most_common()
        filterList = [str(tup[0]) for tup in countlist if int(tup[1]) >= selcount - int(err)]

        self.previewpte.setPlainText(' '.join(filterList))
        self.resultLb.setText(str(len(filterList)) + u'组数据')

        checknum = self.checkNum.text()
        if checknum != '':
            self.highlighter.setHighlightData([checknum])
            self.highlighter.rehighlight()

    @pyqtSlot()
    def on_searchBtn_clicked(self):
        row = self.fileView.rowCount()
        checknum = self.checkNum.text()
        for i in range(row):
            item4 = self.fileView.item(i,  4)
            item2 = self.fileView.item(i,  2)
            content = item4.text()
            contents = content.split(' ')
            if checknum in contents:
                item2.setText('√')
                item2.setForeground(QColor(255,0,0))
            else:
                item2.setText('×')
                item2.setForeground(QColor(0,0,0))

    @pyqtSlot()
    def on_onekeyGlBtn_clicked(self):
        csvlist = []
        checknum = self.checkNum.text()
        if checknum is None or checknum == '':
            reply = QMessageBox.information(self,
                "Warning", u'检验号码不能为空！！')
            return
        for l in common.gelian:
            if l[0] == 0:
                name = u'隔' + str(l[1]) + '连' + str(l[2])
                flag = False
            else:
                name = u'连' + str(l[2]) + '隔' + str(l[1])
                flag = True
            i = 0
            count = 0
            while i < len(self.fileDicts):
                if flag :
                    size = l[2] if i + l[2] < len(self.fileDicts) else len(self.fileDicts) - i

                    for j in range(size):
                        dict = self.fileDicts['seq_' + str(j + i).zfill(4)]
                        if checknum in dict['content'].split(' '):
                            #csvlist.append([name, dict['filename']])
                            count = count + 1
                    i = i + l[2]
                    flag = False
                else:
                    i = i + l[1]
                    flag = True

            csvlist.append([name, str(count)])

        self.saveFileName(DataFrame(csvlist, columns=[u'隔连', u'个数']))

    @pyqtSlot()
    def on_onekeyPcBtn_clicked(self):
        pagesize = self.pagesizeSb.text()
        checknum = self.checkNum.text()
        csvlist = []
        i = 0
        bati = 0
        while i < len(self.fileDicts):
            size = int(pagesize) if i + int(pagesize) < len(self.fileDicts) else len(self.fileDicts) - i
            bati = bati + 1
            for j in range(size):
                name = u'批次' + str(bati)
                dict = self.fileDicts['seq_' + str(j + i).zfill(4)]
                if checknum in dict['content'].split(' '):
                    csvlist.append([name, dict['filename']])
            i = i + int(pagesize)

        self.saveFileName(DataFrame(csvlist, columns=[u'批次', u'文件名']))

    def saveFileName(self, pandas):
        options = QFileDialog.Options()
        fileName, _ = QFileDialog.getSaveFileName(self,
                u"保存文件",
                self.filePathLe.text() + '\\' + self.fileDicts['seq_0001']['filename'][0:-3] if len(self.fileDicts) > 0 else self.filePathLe.text(),
                "Text Files (*.csv)", options=options)
        if fileName is not None and fileName != '':
            pandas.to_csv(fileName)

    def on_folderbtn_clicked(self):
        options = QFileDialog.DontResolveSymlinks | QFileDialog.ShowDirsOnly
        directory = QFileDialog.getExistingDirectory(self, u'选择目录', self.filePathLe.text(), options=options)
        if directory:
            self.filePathLe.setText(directory)

    @pyqtSlot()
    def on_t3_execute_btn_clicked(self):
        self.t3_log_pte.setText('')
        self.activeTab = 3
        filePath = self.filePathLe.text()
        if filePath == '':
            msgBox = QtGui.QMessageBox()
            msgBox.setText(u'导出目录不能为空！')
            msgBox.exec_()
            return False

        thread = TabThread(self)    # create a thread
        thread.trigger.connect(self.logMessage)  # connect to it's signal
        thread.start()             # start the thread
        self.threads.append(thread) # keep a reference
        self.t3_execute_btn.setEnabled(False)

    @pyqtSlot()
    def on_t2_execute_btn_clicked(self):
        self.t2_log_pte.setText('')
        self.activeTab = 2
        filePath = self.filePathLe.text()
        if filePath == '':
            msgBox = QtGui.QMessageBox()
            msgBox.setText(u'导出目录不能为空！')
            msgBox.exec_()
            return False

        thread = TabThread(self)    # create a thread
        thread.trigger.connect(self.logMessage)  # connect to it's signal
        thread.start()             # start the thread
        self.threads.append(thread) # keep a reference
        self.t2_execute_btn.setEnabled(False)

    @pyqtSlot()
    def on_t6_execute_btn_clicked(self):
        self.t6_log_pte.setText('')
        self.activeTab = 6
        filePath = self.filePathLe.text()
        if filePath == '':
            msgBox = QtGui.QMessageBox()
            msgBox.setText(u'导出目录不能为空！')
            msgBox.exec_()
            return False

        if not os.path.exists(filePath):
           msgBox = QtGui.QMessageBox()
           msgBox.setText(u'导出目录不存在！')
           msgBox.exec_()
           return False

        thread = TabThread(self)    # create a thread
        thread.trigger.connect(self.logMessage)  # connect to it's signal
        thread.start()             # start the thread
        self.threads.append(thread) # keep a reference
        self.t6_execute_btn.setEnabled(False)

    @pyqtSlot()
    def on_selectRevBtn_clicked(self):
        resultNum = self.previewpte.toPlainText()
        if '' == resultNum:
            return

        numlist = list(common.getAllAllNum2().number.values)
        numlist = [str(n).zfill(4) for n in numlist]
        resultlist = resultNum.split(' ')
        diffList = list(set(numlist).difference(set(resultlist)))

        self.previewpte.setPlainText(' '.join(diffList))

    @pyqtSlot()
    def on_copybtn_clicked(self):
        self.clipboard.setText(self.previewpte.toPlainText(), QClipboard.Clipboard)
        self.clipboard.setText(self.previewpte.toPlainText(), QClipboard.Selection)

    @pyqtSlot()
    def on_saveBtn_clicked(self):
        options = QFileDialog.Options()
        fileName, _ = QFileDialog.getSaveFileName(self,
                u"保存",
                '',
                "Text Files (*.txt)", options=options)

        if fileName != '':
            with open(fileName, 'w') as inputfile:
                inputfile.write(self.previewpte.toPlainText())

    @pyqtSlot()
    def on_intersetBtn2_clicked(self):
        datadf = self.severDeal()

        if datadf is None:
            return

        datadf = datadf.sort_index(axis=1)
        resultlist = list(datadf.values)
        resultlist = [''.join(map(str, l)) for l in resultlist]
        result = '\n'.join(resultlist)

        options = QFileDialog.Options()
        fileName, _ = QFileDialog.getSaveFileName(self,
                u"保存",
                '',
                "Text Files (*.txt)", options=options)

        if fileName != '':
            with open(fileName, 'w') as inputfile:
                inputfile.write(result)

            self.previewpte2.setText(u'生成' + str(len(resultlist)) + u'组号缁！！')

    @pyqtSlot()
    def on_sub4btn_clicked(self):
        try:
            datadf = self.severDeal()

            if datadf is None:
                return

            datadf = datadf.sort_index(axis=1)
            datadf = datadf.iloc[:,0:4]
            datadf = datadf.drop_duplicates()
            resultlist = list(datadf.values)
            resultlist = [''.join(map(str, l)) for l in resultlist]
            result = '\n'.join(resultlist)

            options = QFileDialog.Options()
            fileName, _ = QFileDialog.getSaveFileName(self,
                    u"保存",
                    '',
                    "Text Files (*.txt)", options=options)

            if fileName != '':
                with open(fileName, 'w') as inputfile:
                    inputfile.write(result)

                self.previewpte2.setText(u'生成' + str(len(resultlist)) + u'组号码！！！')
        except Exception:
            QMessageBox.warning(self,
                    u"警告",
                    u"截取4位出现异常，请确认条件是否满足！",
                    QMessageBox.Yes)

    @pyqtSlot()
    def on_sub5btn_clicked(self):

        try:
            datadf = self.severDeal()

            if datadf is None:
                return

            datadf = datadf.sort_index(axis=1)
            datadf = datadf.iloc[:,0:5]
            datadf = datadf.drop_duplicates()
            resultlist = list(datadf.values)
            resultlist = [''.join(map(str, l)) for l in resultlist]
            result = '\n'.join(resultlist)

            options = QFileDialog.Options()
            fileName, _ = QFileDialog.getSaveFileName(self,
                    u"保存",
                    '',
                    "Text Files (*.txt)", options=options)

            if fileName != '':
                with open(fileName, 'w') as inputfile:
                    inputfile.write(result)

                self.previewpte2.setText(u'生成' + str(len(resultlist)) + u'组号码！！！')
        except Exception:
            QMessageBox.warning(self,
                    u"警告",
                    u"截取5位出现异常，请确认条件是否满足！",
                    QMessageBox.Yes)

    def severDeal(self):
        datadf = None
        isInit = False
        # 1
        place1 = self.placele1.text()
        if place1 != '':
            place1Arr = [list(p) for p in place1.replace('\n','').replace('\r','').split(' ')]
            place1df = DataFrame(place1Arr, columns=['a','b','c','d'])
            if not isInit:
                datadf = place1df.copy()
                isInit = True
            datadf = pd.merge(datadf, place1df)

        # 2
        place2 = self.placele2.text()
        if place2 != '':
            place2Arr = [list(p) for p in place2.replace('\n','').replace('\r','').replace('  ',' ').split(' ')]
            place2df = DataFrame(place2Arr, columns=['a','b','c','e'])
            if not isInit:
                datadf = place2df
                isInit = True
            datadf = pd.merge(datadf, place2df)

        # 3
        place3 = self.placele3.text()
        if place3 != '':
            place3Arr = [list(p) for p in place3.replace('\n','').replace('\r','').replace('  ',' ').split(' ')]
            place3df = DataFrame(place3Arr, columns=['a','b','c','f'])
            if not isInit:
                datadf = place3df
                isInit = True
            datadf = pd.merge(datadf, place3df)

        # 4
        place4 = self.placele4.text()
        if place4 != '':
            place4Arr = [list(p) for p in place4.replace('\n','').replace('\r','').replace('  ',' ').split(' ')]
            place4df = DataFrame(place4Arr, columns=['a','b','c','g'])
            if not isInit:
                datadf = place4df
                isInit = True
            datadf = pd.merge(datadf, place4df)

        # 5
        place5 = self.placele5.text()
        if place5 != '':
            place5Arr = [list(p) for p in place5.replace('\n','').replace('\r','').replace('  ',' ').split(' ')]
            place5df = DataFrame(place5Arr, columns=['a','b','d','e'])
            if not isInit:
                datadf = place5df
                isInit = True
            datadf = pd.merge(datadf, place5df)

        # 6
        place6 = self.placele6.text()
        if place6 != '':
            place6Arr = [list(p) for p in place6.replace('\n','').replace('\r','').replace('  ',' ').split(' ')]
            place6df = DataFrame(place6Arr, columns=['a','b','d','f'])
            if not isInit:
                datadf = place6df
                isInit = True
            datadf = pd.merge(datadf, place6df)

        # 7
        place7 = self.placele7.text()
        if place7 != '':
            place7Arr = [list(p) for p in place7.replace('\n','').replace('\r','').replace('  ',' ').split(' ')]
            place7df = DataFrame(place7Arr, columns=['a','b','d','g'])
            if not isInit:
                datadf = place7df
                isInit = True
            datadf = pd.merge(datadf, place7df)

        # 8
        place8 = self.placele8.text()
        if place8 != '':
            place8Arr = [list(p) for p in place8.replace('\n','').replace('\r','').replace('  ',' ').split(' ')]
            place8df = DataFrame(place8Arr, columns=['a','b','e','f'])
            if not isInit:
                datadf = place8df
                isInit = True
            datadf = pd.merge(datadf, place8df)

        # 9
        place9 = self.placele9.text()
        if place9 != '':
            place9Arr = [list(p) for p in place9.replace('\n','').replace('\r','').replace('  ',' ').split(' ')]
            place9df = DataFrame(place9Arr, columns=['a','b','e','g'])
            if not isInit:
                datadf = place9df
                isInit = True
            datadf = pd.merge(datadf, place9df)

        # 10
        place10 = self.placele10.text()
        if place10 != '':
            place10Arr = [list(p) for p in place10.replace('\n','').replace('\r','').replace('  ',' ').split(' ')]
            place10df = DataFrame(place10Arr, columns=['a','b','f','g'])
            if not isInit:
                datadf = place10df
                isInit = True
            datadf = pd.merge(datadf, place10df)

        # 11
        place11 = self.placele11.text()
        if place11 != '':
            place11Arr = [list(p) for p in place11.replace('\n','').replace('\r','').replace('  ',' ').split(' ')]
            place11df = DataFrame(place11Arr, columns=['a','c','d','e'])
            if not isInit:
                datadf = place11df
                isInit = True
            datadf = pd.merge(datadf, place11df)

        # 12
        place12 = self.placele12.text()
        if place12 != '':
            place12Arr = [list(p) for p in place12.replace('\n','').replace('\r','').replace('  ',' ').split(' ')]
            place12df = DataFrame(place12Arr, columns=['a','c','d','f'])
            if not isInit:
                datadf = place12df
                isInit = True
            datadf = pd.merge(datadf, place12df)

        # 13
        place13 = self.placele13.text()
        if place13 != '':
            place13Arr = [list(p) for p in place13.replace('\n','').replace('\r','').replace('  ',' ').split(' ')]
            place13df = DataFrame(place13Arr, columns=['a','c','d','g'])
            if not isInit:
                datadf = place13df
                isInit = True
            datadf = pd.merge(datadf, place13df)

        # 14
        place14 = self.placele14.text()
        if place14 != '':
            place14Arr = [list(p) for p in place14.replace('\n','').replace('\r','').replace('  ',' ').split(' ')]
            place14df = DataFrame(place14Arr, columns=['a','c','e','f'])
            if not isInit:
                datadf = place14df
                isInit = True
            datadf = pd.merge(datadf, place14df)

        # 15
        place15 = self.placele15.text()
        if place15 != '':
            place15Arr = [list(p) for p in place15.replace('\n','').replace('\r','').replace('  ',' ').split(' ')]
            place15df = DataFrame(place15Arr, columns=['a','c','e','g'])
            if not isInit:
                datadf = place15df
                isInit = True
            datadf = pd.merge(datadf, place15df)

        # 16
        place16 = self.placele16.text()
        if place16 != '':
            place16Arr = [list(p) for p in place16.replace('\n','').replace('\r','').replace('  ',' ').split(' ')]
            place16df = DataFrame(place16Arr, columns=['a','c','f','g'])
            if not isInit:
                datadf = place16df
                isInit = True
            datadf = pd.merge(datadf, place16df)

        # 17
        place17 = self.placele17.text()
        if place17 != '':
            place17Arr = [list(p) for p in place17.replace('\n','').replace('\r','').replace('  ',' ').split(' ')]
            place17df = DataFrame(place17Arr, columns=['a','d','e','f'])
            if not isInit:
                datadf = place17df
                isInit = True
            datadf = pd.merge(datadf, place17df)

        # 18
        place18 = self.placele18.text()
        if place18 != '':
            place18Arr = [list(p) for p in place18.replace('\n','').replace('\r','').replace('  ',' ').split(' ')]
            place18df = DataFrame(place18Arr, columns=['a','d','e','g'])
            if not isInit:
                datadf = place18df
                isInit = True
            datadf = pd.merge(datadf, place18df)

        # 19
        place19 = self.placele19.text()
        if place19 != '':
            place19Arr = [list(p) for p in place19.replace('\n','').replace('\r','').replace('  ',' ').split(' ')]
            place19df = DataFrame(place19Arr, columns=['a','d','f','g'])
            if not isInit:
                datadf = place19df
                isInit = True
            datadf = pd.merge(datadf, place19df)

        # 20
        place20 = self.placele20.text()
        if place20 != '':
            place20Arr = [list(p) for p in place20.replace('\n','').replace('\r','').replace('  ',' ').split(' ')]
            place20df = DataFrame(place20Arr, columns=['a','e','f','g'])
            if not isInit:
                datadf = place20df
                isInit = True
            datadf = pd.merge(datadf, place20df)

        # 21
        place21 = self.placele21.text()
        if place21 != '':
            place21Arr = [list(p) for p in place21.replace('\n','').replace('\r','').replace('  ',' ').split(' ')]
            place21df = DataFrame(place21Arr, columns=['b','c','d','e'])
            if not isInit:
                datadf = place21df
                isInit = True
            datadf = pd.merge(datadf, place21df)

        # 22
        place22 = self.placele22.text()
        if place22 != '':
            place22Arr = [list(p) for p in place22.replace('\n','').replace('\r','').replace('  ',' ').split(' ')]
            place22df = DataFrame(place22Arr, columns=['b','c','d','f'])
            if not isInit:
                datadf = place22df
                isInit = True
            datadf = pd.merge(datadf, place22df)

        # 23
        place23 = self.placele23.text()
        if place23 != '':
            place23Arr = [list(p) for p in place23.replace('\n','').replace('\r','').replace('  ',' ').split(' ')]
            place23df = DataFrame(place23Arr, columns=['b','c','d','g'])
            if not isInit:
                datadf = place23df
                isInit = True
            datadf = pd.merge(datadf, place23df)

        # 24
        place24 = self.placele24.text()
        if place24 != '':
            place24Arr = [list(p) for p in place24.replace('\n','').replace('\r','').replace('  ',' ').split(' ')]
            place24df = DataFrame(place24Arr, columns=['b','c','e','f'])
            if not isInit:
                datadf = place24df
                isInit = True
            datadf = pd.merge(datadf, place24df)

        # 25
        place25 = self.placele25.text()
        if place25 != '':
            place25Arr = [list(p) for p in place25.replace('\n','').replace('\r','').replace('  ',' ').split(' ')]
            place25df = DataFrame(place25Arr, columns=['b','c','e','g'])
            if not isInit:
                datadf = place25df
                isInit = True
            datadf = pd.merge(datadf, place25df)

        # 26
        place26 = self.placele26.text()
        if place26 != '':
            place26Arr = [list(p) for p in place26.replace('\n','').replace('\r','').replace('  ',' ').split(' ')]
            place26df = DataFrame(place26Arr, columns=['b','c','f','g'])
            if not isInit:
                datadf = place26df
                isInit = True
            datadf = pd.merge(datadf, place26df)

        # 27
        place27 = self.placele27.text()
        if place27 != '':
            place27Arr = [list(p) for p in place27.replace('\n','').replace('\r','').replace('  ',' ').split(' ')]
            place27df = DataFrame(place27Arr, columns=['b','d','e','f'])
            if not isInit:
                datadf = place27df
                isInit = True
            datadf = pd.merge(datadf, place27df)

        # 28
        place28 = self.placele28.text()
        if place28 != '':
            place28Arr = [list(p) for p in place28.replace('\n','').replace('\r','').replace('  ',' ').split(' ')]
            place28df = DataFrame(place28Arr, columns=['b','d','e','g'])
            if not isInit:
                datadf = place28df
                isInit = True
            datadf = pd.merge(datadf, place28df)

        # 29
        place29 = self.placele29.text()
        if place29 != '':
            place29Arr = [list(p) for p in place29.replace('\n','').replace('\r','').replace('  ',' ').split(' ')]
            place29df = DataFrame(place29Arr, columns=['b','d','f','g'])
            if not isInit:
                datadf = place29df
                isInit = True
            datadf = pd.merge(datadf, place29df)

        # 30
        place30 = self.placele30.text()
        if place30 != '':
            place30Arr = [list(p) for p in place30.replace('\n','').replace('\r','').replace('  ',' ').split(' ')]
            place30df = DataFrame(place30Arr, columns=['b','e','f','g'])
            if not isInit:
                datadf = place30df
                isInit = True
            datadf = pd.merge(datadf, place30df)

        # 31
        place31 = self.placele31.text()
        if place31 != '':
            place31Arr = [list(p) for p in place31.replace('\n','').replace('\r','').replace('  ',' ').split(' ')]
            place31df = DataFrame(place31Arr, columns=['c','d','e','f'])
            if not isInit:
                datadf = place31df
                isInit = True
            datadf = pd.merge(datadf, place31df)

        # 32
        place32 = self.placele32.text()
        if place32 != '':
            place32Arr = [list(p) for p in place32.replace('\n','').replace('\r','').replace('  ',' ').split(' ')]
            place32df = DataFrame(place32Arr, columns=['c','d','e','g'])
            if not isInit:
                datadf = place32df
                isInit = True
            datadf = pd.merge(datadf, place32df)

        # 33
        place33 = self.placele33.text()
        if place33 != '':
            place33Arr = [list(p) for p in place33.replace('\n','').replace('\r','').replace('  ',' ').split(' ')]
            place33df = DataFrame(place33Arr, columns=['c','d','f','g'])
            if not isInit:
                datadf = place33df
                isInit = True
            datadf = pd.merge(datadf, place33df)

        # 34
        place34 = self.placele34.text()
        if place34 != '':
            place34Arr = [list(p) for p in place34.replace('\n','').replace('\r','').replace('  ',' ').split(' ')]
            place34df = DataFrame(place34Arr, columns=['c','e','f','g'])
            if not isInit:
                datadf = place34df
                isInit = True
            datadf = pd.merge(datadf, place34df)

        # 35
        place35 = self.placele35.text()
        if place35 != '':
            place35Arr = [list(p) for p in place35.replace('\n','').replace('\r','').replace('  ',' ').split(' ')]
            place35df = DataFrame(place35Arr, columns=['d','e','f','g'])
            if not isInit:
                datadf = place35df
                isInit = True
            datadf = pd.merge(datadf, place35df)

        return datadf

class MyHighlighter(QtGui.QSyntaxHighlighter):

    def __init__(self, parent=None):
        QtGui.QSyntaxHighlighter.__init__(self, parent)
        self.parent = parent
        self.highlight_data = []

        self.matched_format = QtGui.QTextCharFormat()
        brush = QtGui.QBrush(QtCore.Qt.yellow, QtCore.Qt.SolidPattern)
        self.matched_format.setBackground(brush)

    def highlightBlock(self, text):
        index = 0
        for item in self.highlight_data:
            index = QRegExp(item).indexIn(text)
            self.setFormat(index, 4, self.matched_format)

        self.setCurrentBlockState(0)

    def setHighlightData(self, highlight_data):
         self.highlight_data = highlight_data

if __name__ == '__main__':
    app = QApplication(sys.argv)
    if Login().exec_():
        mainWin = MainWindow()
        mainWin.show()
        sys.exit(app.exec_())


