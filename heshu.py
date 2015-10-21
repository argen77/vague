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

class heshu(object):
    def __init__(self,parent=None):
        self.heshuresult = []
        self.numbers = common.getAllAllNum()
        self.parent = parent
        self.cvsResultDict = {}

    # 第一（2）步
    def first_2_step(self,filepath,resultdf,conds):
        rstdf = resultdf.groupby('seq').agg(lambda x: ' '.join(x))
        err = 0
        seq = 0
        for index,row in rstdf.iterrows():
            tempcond = {}
            tempcond['ab'] = row['number']
            tempcond['ac'] = row['number']
            tempcond['ad'] = row['number']
            tempcond['bc'] = row['number']
            tempcond['bd'] = row['number']
            tempcond['cd'] = row['number']
            tempcond['error'] = str(err)

            rong = self.twodeal(tempcond, seq)
            seq = seq + 6

        filename = 'pm37R' + str(rong) + '=X60_'
        self.filegenarate(self.getResult(), filepath, filename)

        #oldfilename = 'pm37R'+str(err)+'=%sX60_X%sR%s_'
        oldfilename = 'pm37R'+str(rong)+'=X60_X%sR%s_'
        self.selectedNumAna(filepath,oldfilename,self.getResult(),conds)

    # 第一（3）步
    def first_3_step(self,filepath,resultdf,conds):
        rstdf = resultdf.groupby('seq').agg(lambda x: ' '.join(x))
        err = 0
        seq = 0
        for index,row in rstdf.iterrows():
            tempcond = {}
            tempcond['abc'] = row['number']
            tempcond['abd'] = row['number']
            tempcond['acd'] = row['number']
            tempcond['bcd'] = row['number']
            tempcond['error'] = str(err)

            rong = self.threedeal(tempcond, seq)
            seq = seq + 4

        filename = 'pm37R' + str(rong) + '=X40_'
        self.filegenarate(self.getResult(), filepath, filename)

        #oldfilename = 'pm37R'+str(rong)+'=%sX40_X%sR%s_'
        oldfilename = 'pm37R'+str(rong)+'=X40_X%sR%s_'
        self.selectedNumAna(filepath,oldfilename,self.getResult(),conds)

    # 第二（1）步
    def second_1_step(self,filepath,incond):
        conds = []
        for i in range(10):
            tcond = {}
            tcond['ab'] = ''.join([str((int(n) + i)%10) for n in list(incond['ab'])])
            tcond['ac'] = ''.join([str((int(n) + i)%10) for n in list(incond['ac'])])
            tcond['ad'] = ''.join([str((int(n) + i)%10) for n in list(incond['ad'])])
            tcond['bc'] = ''.join([str((int(n) + i)%10) for n in list(incond['bc'])])
            tcond['bd'] = ''.join([str((int(n) + i)%10) for n in list(incond['bd'])])
            tcond['cd'] = ''.join([str((int(n) + i)%10) for n in list(incond['cd'])])
            tcond['error'] = '2'

            conds.append(tcond)

        seq = 0
        for cond in conds:
            twoList = ['ab', 'ac', 'ad', 'bc', 'bd', 'cd']
            combine = list(itertools.combinations(twoList,6-2))
            self.maindeal2(cond,combine,seq)

            seq = seq + 1

        filename = '2he_R' + str(2) + '=X10_'
        self.filegenarate(self.getResult(), filepath, filename)

    # 第二（2）步  必须基于第二（1）步
    def second_2_step(self,filepath,resultdf,conds):
        rstdf = resultdf.groupby('seq').agg(lambda x: ' '.join(x))
        err = 0
        seq = 0
        for index,row in rstdf.iterrows():
            tempcond = {}
            tempcond['ab'] = row['number']
            tempcond['ac'] = row['number']
            tempcond['ad'] = row['number']
            tempcond['bc'] = row['number']
            tempcond['bd'] = row['number']
            tempcond['cd'] = row['number']
            tempcond['error'] = str(err)

            rong = self.twodeal(tempcond, seq)
            seq = seq + 6

        filename = '2he26o30R' + str(rong) + '=X60_'
        self.filegenarate(self.getResult(), filepath, filename)

        #oldfilename = '2he26o30R'+str(err)+'=%sX60_X%sR%s_'
        #oldfilename = '2he26o30R'+str(rong)+'=X60_X%sR%s_'
        #self.selectedNumAna(filepath,oldfilename,self.getResult(),conds)

    # 第二（3）步  必须基于第二（1）步
    def second_3_step(self,filepath,resultdf,conds):
        rstdf = resultdf.groupby('seq').agg(lambda x: ' '.join(x))
        err = 0
        seq = 0
        for index,row in rstdf.iterrows():
            tempcond = {}
            tempcond['abc'] = row['number']
            tempcond['abd'] = row['number']
            tempcond['acd'] = row['number']
            tempcond['bcd'] = row['number']
            tempcond['error'] = str(err)

            rong = self.threedeal(tempcond, seq)
            seq = seq + 4

        filename = '2he26o30R=X40_'
        self.filegenarate(self.getResult(), filepath, filename)

        #oldfilename = '2he26o30R'+str(rong)+'=%sX40_X%sR%s_'
        #oldfilename = '2he26o30R'+str(rong)+'=X40_X%sR%s_'
        #self.selectedNumAna(filepath,oldfilename,self.getResult(),conds)

    #第二（4）步 第二（5）步
    def second_45_step(self,filepath,incond):
        conds = []
        for i in range(10):
            tcond = {}
            tcond['ab'] = ''.join([str((int(n) + i)%10) for n in list(incond['ab'])])
            tcond['ac'] = ''.join([str((int(n) + i)%10) for n in list(incond['ac'])])
            tcond['ad'] = ''.join([str((int(n) + i)%10) for n in list(incond['ad'])])
            tcond['bc'] = ''.join([str((int(n) + i)%10) for n in list(incond['bc'])])
            tcond['bd'] = ''.join([str((int(n) + i)%10) for n in list(incond['bd'])])
            tcond['cd'] = ''.join([str((int(n) + i)%10) for n in list(incond['cd'])])
            tcond['error'] = '5'

            conds.append(tcond)

        seq = 0
        for cond in conds:
            twoList = ['ab', 'ac', 'ad', 'bc', 'bd', 'cd']
            combine = list(itertools.combinations(twoList,6-5))
            self.maindeal2(cond,combine,seq)

            seq = seq + 1

        resultdf = self.getResult()

        filename = '2he_R5=X10_'
        self.filegenarate(self.getResult(), filepath, filename)

        oldfilename = '2heR'+str(5)+'=X10_X%sR%s_'
        self.selectedNumAna(filepath,oldfilename,resultdf,incond)

    # 第三（1）步
    def three_1_step(self,filepath,incond):
        conds = []
        for i in range(10):
            tcond = {}
            tcond['abc'] = ''.join([str((int(n) + i)%10) for n in list(incond['abc'])])
            tcond['abd'] = ''.join([str((int(n) + i)%10) for n in list(incond['abd'])])
            tcond['acd'] = ''.join([str((int(n) + i)%10) for n in list(incond['acd'])])
            tcond['bcd'] = ''.join([str((int(n) + i)%10) for n in list(incond['bcd'])])
            tcond['error'] = '1'

            conds.append(tcond)

        seq = 0
        for cond in conds:
            twoList = ['abc', 'abd', 'acd', 'bcd']
            combine = list(itertools.combinations(twoList,4-1))
            self.maindeal2(cond,combine,seq)

            seq = seq + 1

        filename = '3heR' + str(1) + '=X10_'
        self.filegenarate(self.getResult(), filepath, filename)

    # 第三（2）步  必须基于第三（1）步
    def three_2_step(self,filepath,resultdf,conds):
        rstdf = resultdf.groupby('seq').agg(lambda x: ' '.join(x))
        err = 0
        seq = 0
        for index,row in rstdf.iterrows():
            tempcond = {}
            tempcond['ab'] = row['number']
            tempcond['ac'] = row['number']
            tempcond['ad'] = row['number']
            tempcond['bc'] = row['number']
            tempcond['bd'] = row['number']
            tempcond['cd'] = row['number']
            tempcond['error'] = str(err)

            rong = self.twodeal(tempcond, seq)
            seq = seq + 6

        filename = '3he37R' + str(rong) + '=X60_'
        self.filegenarate(self.getResult(), filepath, filename)

    # 第三（3）步  必须基于第三（1）步
    def three_3_step(self,filepath,resultdf,conds):
        rstdf = resultdf.groupby('seq').agg(lambda x: ' '.join(x))
        err = 0
        seq = 0
        for index,row in rstdf.iterrows():
            tempcond = {}
            tempcond['abc'] = row['number']
            tempcond['abd'] = row['number']
            tempcond['acd'] = row['number']
            tempcond['bcd'] = row['number']
            tempcond['error'] = str(err)

            self.threedeal(tempcond, seq)
            seq = seq + 4

        filename = '3he37R=X40_'
        self.filegenarate(self.getResult(), filepath, filename)

    #第三（4）步 第三（5）步
    def three_45_step(self,filepath,incond):
        conds = []
        for i in range(10):
            tcond = {}
            tcond['abc'] = ''.join([str((int(n) + i)%10) for n in list(incond['abc'])])
            tcond['abd'] = ''.join([str((int(n) + i)%10) for n in list(incond['abd'])])
            tcond['acd'] = ''.join([str((int(n) + i)%10) for n in list(incond['acd'])])
            tcond['bcd'] = ''.join([str((int(n) + i)%10) for n in list(incond['bcd'])])
            tcond['error'] = '3'

            conds.append(tcond)

        seq = 0
        for cond in conds:
            twoList = ['abc', 'abd', 'acd', 'bcd']
            combine = list(itertools.combinations(twoList,1))
            self.maindeal2(cond,combine,seq)

            seq = seq + 1

        resultdf = self.getResult()

        filename = '3heR3=X10_'
        self.filegenarate(self.getResult(), filepath, filename)

        #oldfilename = '3heR'+str(3)+'=%sX10_X%sR%s_'
        oldfilename = '3heR'+str(3)+'=X10_X%sR%s_'
        self.selectedNumAna(filepath,oldfilename,resultdf,incond)

    def four_1_step(self,filepath,pmresult, h2result, incond):
        h2resulttemp = h2result.applymap(self.addSeq)
        resultdf = pd.concat([pmresult, h2resulttemp])
        if common.debugOn:
            common.logging.debug("resultdf :")
            common.logging.debug(resultdf)

        oldfilename = 'pm+2heX20_X%sR%s_'
        self.selectedNumAna(filepath,oldfilename,resultdf,incond)

    def four_2_step(self,filepath,pmresult, h3result, incond):
        h3resulttemp = h3result.applymap(self.addSeq)
        resultdf = pd.concat([pmresult, h3resulttemp])

        #oldfilename = 'pm+3heX%s_X%sR%s_'
        oldfilename = 'pm+3heX20_X%sR%s_'
        self.selectedNumAna(filepath,oldfilename,resultdf,incond)

    def four_3_step(self,filepath,h2result, h3result, incond):
        h3resulttemp = h3result.applymap(self.addSeq)
        resultdf = pd.concat([h2result, h3resulttemp])

        #oldfilename = '3he+2heX%s_X%sR%s_'
        oldfilename = '3he+2heX20_X%sR%s_'
        self.selectedNumAna(filepath,oldfilename,resultdf,incond)

    def four_4_step(self,filepath,pmresult,h2result,h3result,incond):
        h2result = h2result.applymap(self.addSeq)
        h3result = h3result.applymap(self.addSeq2)
        resultdf = pd.concat([pmresult, h2result, h3result])

        #oldfilename = '3he+2heX%s_X%sR%s_'
        oldfilename = 'pm+2he+3heX30_X%sR%s_'
        self.selectedNumAna(filepath,oldfilename,resultdf,incond)

    # 第四（5）步
    def four_57_step(self,filepath,resultdf,step):
        rstdf = resultdf.groupby('seq').agg(lambda x: ' '.join(x))
        err = 0
        seq = 0
        for index,row in rstdf.iterrows():
            self.maindeal(row['number'], 'ab', err, seq)
            self.maindeal(row['number'], 'ac', err, seq)
            self.maindeal(row['number'], 'ad', err, seq)
            self.maindeal(row['number'], 'bc', err, seq)
            self.maindeal(row['number'], 'bd', err, seq)
            self.maindeal(row['number'], 'cd', err, seq)
            seq = seq + 1

        if step == '5':
            filename = 'pm37X10LSH=X10_'
        else:
            filename = '2he26or30X10LSH=X10_'
        self.filegenarate(self.getResult(), filepath, filename)

    # 第四（6）步
    def four_68_step(self,filepath,resultdf,step):
        rstdf = resultdf.groupby('seq').agg(lambda x: ' '.join(x))
        err = 0
        seq = 0
        for index,row in rstdf.iterrows():
            self.maindeal(row['number'], 'abc', err, seq)
            self.maindeal(row['number'], 'abd', err, seq)
            self.maindeal(row['number'], 'acd', err, seq)
            self.maindeal(row['number'], 'bcd', err, seq)
            seq = seq + 1

        if step == '6':
            filename = 'pm37X10SSH_X10_'
        else:
            filename = '2he26or30X10SSH=X10_'
        self.filegenarate(self.getResult(), filepath, filename)

    def selectedNumAna(self,filepath,oldfilename,resultdf,incond):
        if common.debugOn:
            common.logging.debug('resultdf len :' + str(len(list(resultdf.number.values))))
        #resultdf = self.getResult()
        groupbybf = resultdf.groupby('seq')
        if len(groupbybf) > 10:
            jhsel = len(groupbybf) - 2
            jherr = len(groupbybf) - 4
        else:
            jhsel = len(groupbybf)
            jherr = len(groupbybf) - 2

        #oldfilename = '3heR'+incond['h3err']+'=%sX10_X%sR%s_'
        #filecount = jhsel
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

    def twodeal(self,cond,seq):
        self.maindeal(cond['ab'], 'ab', int(cond['error']), seq+0)
        self.maindeal(cond['ac'], 'ac', int(cond['error']), seq+1)
        self.maindeal(cond['ad'], 'ad', int(cond['error']), seq+2)
        self.maindeal(cond['bc'], 'bc', int(cond['error']), seq+3)
        self.maindeal(cond['bd'], 'bd', int(cond['error']), seq+4)
        err = self.maindeal(cond['cd'], 'cd', int(cond['error']), seq+5)

        return err

    def threedeal(self,cond,seq):
        self.maindeal(cond['abc'], 'abc', int(cond['error']), seq+0)
        self.maindeal(cond['abd'], 'abd', int(cond['error']), seq+1)
        self.maindeal(cond['acd'], 'acd', int(cond['error']), seq+2)
        err = self.maindeal(cond['bcd'], 'bcd', int(cond['error']), seq+3)

        return err

    def maindeal(self, cond, column, err, seq):
        condsplit = [list(set(list(x))) for x in cond.split(' ')]
        #print(condsplit)
        for x in condsplit:
            if len(x) == 3:
                x.append(99)
            elif len(x) == 2:
                x.append(99)
                x.append(99)
            elif len(x) == 1:
                x.append(99)
                x.append(99)
                x.append(99)
        tempnp = np.array(condsplit).reshape(len(condsplit) * len(condsplit[0]))
        counts = Counter(tempnp.tolist())
        mostcount = counts.most_common()
        #print(mostcount)
        temperr = err
        while temperr < 37:
            selcond = [int(x[0]) for x in mostcount if x[1] >= len(condsplit) - int(temperr) and x[0] != '99']
            if len(selcond) == 0:
                temperr = temperr + 1
            else:
                break

        filternum = self.numbers[(self.numbers[column]%10).isin(selcond)]
        for i in range(len(filternum)):
            resultdata = {}
            resultdata['number'] = str(filternum.iat[i,0]) + str(filternum.iat[i,1]) + str(filternum.iat[i,2]) + str(filternum.iat[i,3])
            resultdata['seq'] = str(seq)

            self.heshuresult.append(resultdata)

        return str(temperr)

        #for x in selcond:
        #    filternum = self.numbers[self.numbers[column]%10 == int(x)]

    def maindeal2(self, cond, columns,seq):
        for cols in columns:
            filternum = self.numbers.copy()
            for col in cols:
                filternum = filternum[(filternum[col]%10).isin(map(int, list(cond[col])))]

            for i in range(len(filternum)):
                resultdata = {}
                resultdata['number'] = str(filternum.iat[i,0]) + str(filternum.iat[i,1]) + str(filternum.iat[i,2]) + str(filternum.iat[i,3])
                resultdata['seq'] = str(seq)

                self.heshuresult.append(resultdata)

    def filegenarate(self, df, filepath, filename):
        if len(df) == 0: return
        groupdf = df.groupby('seq').agg(lambda x: ' '.join(x))
        for index,row in groupdf.iterrows():
            #filenameI = (filename % str(len(row['number'].split(' '))))
            tempfilename = filepath + '\\' + filename + str(int(index)+1).zfill(2) + '.txt'
            with open(tempfilename, 'w') as inputfile:
                inputfile.write(row['number'])

            #if not self.parent is None:
            #    self.parent.trigger.emit(u'生成文件：' + tempfilename)

    def getResult(self):
        resultdf = DataFrame(self.heshuresult)
        return resultdf.drop_duplicates() if len(resultdf) > 0 else resultdf

    def clearResultList(self):
        self.heshuresult = []

    def addSeq(self,x):
        if len(str(x)) < 4:
            return str(int(x) + 10)
        else:
            return str(x)

    def addSeq2(self,x):
        if len(str(x)) < 4:
            return str(int(x) + 20)
        else:
            return str(x)

    def removeErrFile(self, filename):
        files=glob.glob(u'' + filename)
        #print(files)
        for f in files:
            os.remove(f)

    def statistics(self, filepath, cond):
        statisList = []
        for k in sorted(self.cvsResultDict.keys()):
            keys = k.split('_')
            l = [common.stepname[keys[0]], keys[1].replace('x', u'选').replace('r', u'容'), self.cvsResultDict[k]]
            statisList.append(l)

        filename = filepath + '\\' + u'检验'+str(cond['checknum']) + '.csv'
        statisdf = DataFrame(statisList, columns=[u'步骤', u'选容', u'个数'])

        statisdf.to_csv(filename)

    def addcsvDict(self, adddict):
        self.cvsResultDict.update(adddict)

if __name__ == '__main__':
    starttime = datetime.now()
    conds = {'ab':'0234 1034 1134 1204 1214 1224 1230 1231 1232 1233 1234 1235 1236 1237 1238 1239 1244 1254 1264 1274 1284 1294 1334 1434 1534 1634 1734 1834 1934 2234 3234 4234 5234 6234 7234 8234 9234',
             'ac':'0234 1034 1134 1204 1214 1224 1230 1231 1232 1233 1234 1235 1236 1237 1238 1239 1244 1254 1264 1274 1284 1294 1334 1434 1534 1634 1734 1834 1934 2234 3234 4234 5234 6234 7234 8234 9234',
             'ad':'0234 1034 1134 1204 1214 1224 1230 1231 1232 1233 1234 1235 1236 1237 1238 1239 1244 1254 1264 1274 1284 1294 1334 1434 1534 1634 1734 1834 1934 2234 3234 4234 5234 6234 7234 8234 9234',
             'bc':'0234 1034 1134 1204 1214 1224 1230 1231 1232 1233 1234 1235 1236 1237 1238 1239 1244 1254 1264 1274 1284 1294 1334 1434 1534 1634 1734 1834 1934 2234 3234 4234 5234 6234 7234 8234 9234',
             'bd':'0234 1034 1134 1204 1214 1224 1230 1231 1232 1233 1234 1235 1236 1237 1238 1239 1244 1254 1264 1274 1284 1294 1334 1434 1534 1634 1734 1834 1934 2234 3234 4234 5234 6234 7234 8234 9234',
             'cd':'0234 1034 1134 1204 1214 1224 1230 1231 1232 1233 1234 1235 1236 1237 1238 1239 1244 1254 1264 1274 1284 1294 1334 1434 1534 1634 1734 1834 1934 2234 3234 4234 5234 6234 7234 8234 9234',
             'abc':'0234 1034 1134 1204 1214 1224 1230 1231 1232 1233 1234 1235 1236 1237 1238 1239 1244 1254 1264 1274 1284 1294 1334 1434 1534 1634 1734 1834 1934 2234 3234 4234 5234 6234 7234 8234 9234',
             'abd':'0234 1034 1134 1204 1214 1224 1230 1231 1232 1233 1234 1235 1236 1237 1238 1239 1244 1254 1264 1274 1284 1294 1334 1434 1534 1634 1734 1834 1934 2234 3234 4234 5234 6234 7234 8234 9234',
             'acd':'0234 1034 1134 1204 1214 1224 1230 1231 1232 1233 1234 1235 1236 1237 1238 1239 1244 1254 1264 1274 1284 1294 1334 1434 1534 1634 1734 1834 1934 2234 3234 4234 5234 6234 7234 8234 9234',
             'bcd':'0234 1034 1134 1204 1214 1224 1230 1231 1232 1233 1234 1235 1236 1237 1238 1239 1244 1254 1264 1274 1284 1294 1334 1434 1534 1634 1734 1834 1934 2234 3234 4234 5234 6234 7234 8234 9234',
             'error':'9'}
    heshu = heshu()
    #heshu.maindeal(conds['ab'], 'ab', conds['error'], '0')
    heshu.twodeal(conds, 0)
    #heshu.threedeal(conds, 0)
    condlist = []
    condlist.append(conds)
    #heshu.first_2_step('D:\\Temp\\test', condlist)
    #heshu.first_3_step('D:\\Temp\\test', condlist)
    df = heshu.getResult().applymap(heshu.addSeq)
    print(df)
    endtime = datetime.now()
    tend = endtime - starttime
    print(u'执行时间：'+str(tend.seconds)+u'秒')
