#!/usr/bin/env python
# -*- coding: utf-8 -*-

from collections import Counter
import numpy as np
import common
from datetime import datetime
from pandas import DataFrame
import os
import glob
import sys
import itertools
import pandas as pd

class peima(object):
    def __init__(self,parent=None):
        self.peimaresult = []
        self.numbers = common.getAllAllNum()
        self.parent = parent
        self.cvsResultDict = {}

    # 第一（1）步
    def first_1_step(self,filepath,cond):
        filename = 'pm_R' + str(cond['err1']) + '=X10_'
        self.tenCircle(cond)
        resultdf = self.getResult()
        self.filegenarate(resultdf, filepath, filename)

    # 第一（4）步 第一（5）步
    def first_45_step(self,filepath,incond):
        self.tenCircle(incond)
        resultdf = self.getResult()
        filename4 = 'pm_R' + str(incond['err1']) + '=X10_'
        self.filegenarate(resultdf, filepath, filename4)
        groupbybf = resultdf.groupby('seq')

        if len(groupbybf) > 10:
            jhsel = len(groupbybf) - 2
            jherr = len(groupbybf) - 4
        else:
            jhsel = len(groupbybf)
            jherr = len(groupbybf) - 2

        oldfilename = 'pmR3=X10_X%sR%s_'

        for filecount in list(reversed(range(2, jhsel + 1))):
            rong = filecount-1 if jherr >= filecount else jherr
            seqlist = range(filecount)
            rList = list(reversed(range(rong)))
            missList = []
            for i in range(len(groupbybf)):
                paramvar = [str((x+i)%len(groupbybf)) for x in seqlist]
                filterdf = resultdf[resultdf['seq'].isin(paramvar)]
                countlist = Counter(list(filterdf.number.values))
                countlist = countlist.most_common()

                if common.debugOn:
                    common.logging.debug(str(len(list(filterdf.number.values))))

                for r in rList:
                    if r in missList:
                        continue
                    concatList = [str(tup[0]) for tup in countlist if int(tup[1]) >= filecount-r]
                    resultstr = ' '.join(concatList)

                    filename = (oldfilename % (str(filecount), str(r)))
                    tempfilename = filepath + '\\' + filename + str(i + 1).zfill(2) + '.txt'
                    if len(concatList) < 22 or len(concatList) > 9899:
                        missList.append(r)
                        if tempfilename != '' and len(tempfilename) > 6:
                            delfile = tempfilename[0:-6] + '*'
                            #if not self.parent is None:
                            #    self.parent.trigger.emit(u'不全项，删除文件名：'+ delfile)
                            self.removeErrFile(delfile)

                        key = incond['step'] + '_x' + str(filecount) + 'r' + str(r)
                        if key in self.cvsResultDict:
                            del self.cvsResultDict[key]
                        if len(concatList) < 22:
                            break
                        else:
                            continue

                    # 生成TXT文件
                    with open(tempfilename, 'w') as inputfile:
                        inputfile.write(resultstr)

                    # 统计校验号码个数
                    checknum = incond['checknum']
                    if checknum in resultstr.split(' ') :
                        key = incond['step'] + '_x' + str(filecount) + 'r' + str(r)
                        if key in self.cvsResultDict:
                            self.cvsResultDict[key] = self.cvsResultDict[key] + 1
                        else:
                            self.cvsResultDict[key] = 1
                    else:
                        key = incond['step'] + '_x' + str(filecount) + 'r' + str(r)
                        if  key not in self.cvsResultDict:
                            self.cvsResultDict[key] = 0

        #print(u'第一（4）步处理完成。')

    def tenCircle(self, cond):
        for i in range(10):
            tcond = {}
            tcond['num1'] = ''.join([str((int(n) + i)%10) for n in list(cond['num1'])])
            tcond['num2'] = ''.join([str((int(n) + i)%10) for n in list(cond['num2'])])
            tcond['num3'] = ''.join([str((int(n) + i)%10) for n in list(cond['num3'])])
            tcond['num4'] = ''.join([str((int(n) + i)%10) for n in list(cond['num4'])])
            tcond['error'] = cond['err1']

            #print(tcond)
            self.maindeal(tcond, i)

    def maindeal(self,cond,seq):
        for index,row in self.numbers.iterrows():
            num1 = row['num1']
            num2 = row['num2']
            num3 = row['num3']
            num4 = row['num4']
            j = 0
            if str(num1) not in list(str(cond['num1'])):
                j += 1
            if str(num2) not in list(str(cond['num2'])):
                j += 1
            if str(num3) not in list(str(cond['num3'])):
                j += 1
            if str(num4) not in list(str(cond['num4'])):
                j += 1

            resultdata = {}
            if j <= int(cond['error']):
                resultdata['number'] = str(num1) + str(num2) + str(num3) + str(num4)
                #resultdata['filename'] = 'PM_R'+str(cond['error'])+'X10'+'_'+str(seq+1).zfill(2)
                resultdata['seq'] = str(seq)

                self.peimaresult.append(resultdata)

        #newNumbers = self.numbers.apply(self.checkerr, conds=cond, axis=1)
        #newNumbers = newNumbers[newNumbers['flag'] == 'True']
        #print(newNumbers)

    def checkerr(self,x,conds):
        flag = 0
        if str(x['num1']) not in list(str(conds['num1'])):
            flag += 1
        if str(x['num2']) not in list(str(conds['num2'])):
            flag += 1
        if str(x['num3']) not in list(str(conds['num3'])):
            flag += 1
        if str(x['num4']) not in list(str(conds['num4'])):
            flag += 1

        x['flag'] = 'True' if flag <= int(conds['error']) else 'Flase'
        return x

    def filegenarate(self, df, filepath, filename):
        groupdf = df.groupby('seq').agg(lambda x: ' '.join(x))
        for index,row in groupdf.iterrows():
            #filenameI = (filename % str(len(row['number'].split(' '))))
            tempfilename = filepath + '\\' + filename + str(int(index)+1).zfill(2) + '.txt'
            with open(tempfilename, 'w') as inputfile:
                inputfile.write(row['number'])

            #if not self.parent is None:
            #    self.parent.trigger.emit(u'生成文件：' + tempfilename)

    def removeErrFile(self, filename):
        files=glob.glob(u'' + filename)
        for f in files:
            os.remove(f)

    def getResult(self):
        return DataFrame(self.peimaresult)

    def clearResultList(self):
        self.peimaresult = []

    def getcsvDict(self):
        return self.cvsResultDict

if __name__ == '__main__':
    starttime = datetime.now()
    #print(common.getAllAllNum())
    cond = {'num1':'1','num2':'2','num3':'3','num4':'4','error':3,'jhsel':10,'jherr':8}
    #cond = ''.join([str((int(n) + 1)%10) for n in list(cond['num1'])])
    #print(cond)
    peima = peima()
    #peima.tenCircle(cond)
    #peima.maindeal(cond,0)
    #df = DataFrame(peima.getResult())
    #print(df.groupby('seq').agg(lambda x: ' '.join(x)))
    #peima.first_1_step('D:\\Temp\\test', cond)
    peima.first_45_step('D:\\Temp\\test', cond)
    print(len(peima.getResult()))
    endtime = datetime.now()
    tend = endtime - starttime
    print(u'执行时间：'+str(tend.seconds)+u'秒')



