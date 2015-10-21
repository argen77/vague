#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import common
from peima import peima
from heshu import heshu
from datetime import datetime

def first(cond, filepath, parent):
    pm = peima(parent)
    hs = heshu(parent)
    pm.first_1_step(filepath, cond)
    pmrst = pm.getResult()
    hs.first_2_step(filepath,pmrst,cond)
    hs.clearResultList()
    hs.first_3_step(filepath, pmrst, cond)

def first45(cond):
    pm = peima()
    pm.first_45_step('D:\\Temp\\test', cond)

def second(cond, filepath, parent):
    hs = heshu(parent)
    hs.second_1_step(filepath, cond)
    hsrst = hs.getResult().copy()
    hs.clearResultList()
    hs.second_2_step(filepath, hsrst, cond)
    hs.clearResultList()
    hs.second_3_step(filepath, hsrst, cond)

def second45(cond):
    hs = heshu()
    hs.second_45_step('F:\\test', cond)

def three(cond):
    hs = heshu()
    hs.three_1_step('F:\\test',cond)
    hsrst = hs.getResult().copy()
    hs.clearResultList()
    hs.three_2_step('F:\\test', hsrst, cond)
    hs.clearResultList()
    hs.three_3_step('F:\\test', hsrst, cond)

def three45(cond):
    hs = heshu()
    hs.three_45_step('F:\\test', cond)

def oneKey(cond, filepath, parent):
    pm = peima(parent)
    hs = heshu(parent)
    cond['err1'] = '1'

    ####################################################
    ## 第一（1）步
    ####################################################
    if not parent is None:
        parent.trigger.emit(u'第一（1）步开始执行，请稍等...')

    if common.debugOn:
        common.logging.debug(u'/**************第一（1）步****************/')

    cond['step'] = '11'

    tempfilePath = filepath + '\\' + u'第一（1）步'
    if not os.path.exists(tempfilePath):
        os.mkdir(tempfilePath)

    pm.first_1_step(tempfilePath, cond)
    pmrst1 = pm.getResult().copy()

    if not parent is None:
        parent.trigger.emit(u'第一（1）步执行结束！')

    ####################################################
    ## 第一（2）步
    ####################################################
    if not parent is None:
        parent.trigger.emit(u'第一（2）步开始执行，请稍等...')

    if common.debugOn:
        common.logging.debug(u'/**************第一（2）步****************/')

    cond['step'] = '12'

    tempfilePath = filepath + '\\' + u'第一（2）步'
    if not os.path.exists(tempfilePath):
        os.mkdir(tempfilePath)

    hs.first_2_step(tempfilePath,pmrst1,cond)

    if not parent is None:
        parent.trigger.emit(u'第一（2）步执行结束！')

    ####################################################
    ## 第一（3）步
    ####################################################
    if not parent is None:
        parent.trigger.emit(u'第一（3）步开始执行，请稍等...')

    if common.debugOn:
        common.logging.debug(u'/**************第一（3）步****************/')

    cond['step'] = '13'

    tempfilePath = filepath + '\\' + u'第一（3）步'

    if not os.path.exists(tempfilePath):
        os.mkdir(tempfilePath)
    hs.clearResultList()
    hs.first_3_step(tempfilePath, pmrst1, cond)

    if not parent is None:
        parent.trigger.emit(u'第一（3）步执行结束！')
    ####################################################
    ## 第一（4）步
    ####################################################
    if not parent is None:
        parent.trigger.emit(u'第一（4）步开始执行，请稍等...')

    if common.debugOn:
        common.logging.debug(u'/**************第一（4）步****************/')

    cond['step'] = '14'

    tempfilePath = filepath + '\\' + u'第一（4）步'

    if not os.path.exists(tempfilePath):
        os.mkdir(tempfilePath)
    cond['err1'] = '3'
    pm.clearResultList()
    pm.first_45_step(tempfilePath, cond)
    pmrst145 = pm.getResult().copy()

    if not parent is None:
        parent.trigger.emit(u'第一（4）步执行结束！')
    ####################################################
    ## 第二（1）步
    ####################################################
    if not parent is None:
        parent.trigger.emit(u'第二（1）步开始执行，请稍等...')

    if common.debugOn:
        common.logging.debug(u'/**************第二（1）步****************/')

    cond['step'] = '21'

    tempfilePath = filepath + '\\' + u'第二（1）步'

    if not os.path.exists(tempfilePath):
        os.mkdir(tempfilePath)
    hs.clearResultList()
    hs.second_1_step(tempfilePath, cond)
    hsrst2 = hs.getResult().copy()

    if not parent is None:
        parent.trigger.emit(u'第二（1）步执行结束！')
    ####################################################
    ## 第二（2）步
    ####################################################
    if not parent is None:
        parent.trigger.emit(u'第二（2）步开始执行，请稍等...')

    if common.debugOn:
        common.logging.debug(u'/**************第二（2）步****************/')

    cond['step'] = '22'

    tempfilePath = filepath + '\\' + u'第二（2）步'

    if not os.path.exists(tempfilePath):
        os.mkdir(tempfilePath)
    hs.clearResultList()
    #print(u'第二（2）步  结果长度：' + str(len(hsrst2)))
    #print(hsrst2)
    hs.second_2_step(tempfilePath, hsrst2, cond)

    if not parent is None:
        parent.trigger.emit(u'第二（2）步执行结束！')
    ####################################################
    ## 第二（3）步
    ####################################################
    if not parent is None:
        parent.trigger.emit(u'第二（3）步开始执行，请稍等...')

    if common.debugOn:
        common.logging.debug(u'/**************第二（3）步****************/')

    cond['step'] = '23'

    tempfilePath = filepath + '\\' + u'第二（3）步'

    if not os.path.exists(tempfilePath):
        os.mkdir(tempfilePath)
    hs.clearResultList()
    hs.second_3_step(tempfilePath, hsrst2, cond)

    if not parent is None:
        parent.trigger.emit(u'第二（3）步执行结束！')
    ####################################################
    ## 第二（4）步
    ####################################################
    if not parent is None:
        parent.trigger.emit(u'第二（4）步开始执行，请稍等...')

    if common.debugOn:
        common.logging.debug(u'/**************第二（4）步****************/')

    cond['step'] = '24'

    tempfilePath = filepath + '\\' + u'第二（4）步'

    if not os.path.exists(tempfilePath):
        os.mkdir(tempfilePath)
    hs.clearResultList()
    hs.second_45_step(tempfilePath, cond)
    hsrst245 = hs.getResult().copy()

    if not parent is None:
        parent.trigger.emit(u'第二（4）步执行结束！')
    ####################################################
    ## 第三（1）步
    ####################################################
    if not parent is None:
        parent.trigger.emit(u'第三（1）步开始执行，请稍等...')

    if common.debugOn:
        common.logging.debug(u'/**************第三（1）步****************/')

    cond['step'] = '31'

    tempfilePath = filepath + '\\' + u'第三（1）步'

    if not os.path.exists(tempfilePath):
        os.mkdir(tempfilePath)
    hs.clearResultList()
    hs.three_1_step(tempfilePath,cond)
    hsrst3 = hs.getResult().copy()

    if not parent is None:
        parent.trigger.emit(u'第三（1）步执行结束！')
    ####################################################
    ## 第三（2）步
    ####################################################
    if not parent is None:
        parent.trigger.emit(u'第三（2）步开始执行，请稍等...')

    if common.debugOn:
        common.logging.debug(u'/**************第三（2）步****************/')

    cond['step'] = '32'

    tempfilePath = filepath + '\\' + u'第三（2）步'

    if not os.path.exists(tempfilePath):
        os.mkdir(tempfilePath)
    hs.clearResultList()
    print(u'第三（1）步  结果长度：' + str(len(hsrst3)))
    print(hsrst3)
    hs.three_2_step(tempfilePath, hsrst3, cond)

    if not parent is None:
        parent.trigger.emit(u'第三（2）步执行结束！')
    ####################################################
    ## 第三（3）步
    ####################################################
    if not parent is None:
        parent.trigger.emit(u'第三（3）步开始执行，请稍等...')

    if common.debugOn:
        common.logging.debug(u'/**************第三（3）步****************/')

    cond['step'] = '33'

    tempfilePath = filepath + '\\' + u'第三（3）步'

    if not os.path.exists(tempfilePath):
        os.mkdir(tempfilePath)
    hs.clearResultList()
    hs.three_3_step(tempfilePath, hsrst3, cond)

    if not parent is None:
        parent.trigger.emit(u'第三（3）步执行结束！')
    ####################################################
    ## 第三（4）步
    ####################################################
    if not parent is None:
        parent.trigger.emit(u'第三（4）步开始执行，请稍等...')

    if common.debugOn:
        common.logging.debug(u'/**************第三（4）步****************/')

    cond['step'] = '34'

    tempfilePath = filepath + '\\' + u'第三（4）步'

    if not os.path.exists(tempfilePath):
        os.mkdir(tempfilePath)
    hs.clearResultList()
    hs.three_45_step(tempfilePath, cond)
    hsrst345 = hs.getResult().copy()

    if not parent is None:
        parent.trigger.emit(u'第三（4）步执行结束！')
    ####################################################
    ## 第四（1）步
    ####################################################
    if not parent is None:
        parent.trigger.emit(u'第四（1）步开始执行，请稍等...')

    if common.debugOn:
        common.logging.debug(u'/**************第四（1）步****************/')

    cond['step'] = '41'

    tempfilePath = filepath + '\\' + u'第四（1）步'

    if not os.path.exists(tempfilePath):
        os.mkdir(tempfilePath)
    hs.clearResultList()
    hs.four_1_step(tempfilePath, pmrst145, hsrst245, cond)

    if not parent is None:
        parent.trigger.emit(u'第四（1）步执行结束！')
    ####################################################
    ## 第四（2）步
    ####################################################
    if not parent is None:
        parent.trigger.emit(u'第四（2）步开始执行，请稍等...')

    if common.debugOn:
        common.logging.debug(u'/**************第四（2）步****************/')

    cond['step'] = '42'

    tempfilePath = filepath + '\\' + u'第四（2）步'

    if not os.path.exists(tempfilePath):
        os.mkdir(tempfilePath)
    hs.clearResultList()
    hs.four_2_step(tempfilePath, pmrst145, hsrst345, cond)

    if not parent is None:
        parent.trigger.emit(u'第四（2）步执行结束！')
    ####################################################
    ## 第四（3）步
    ####################################################
    if not parent is None:
        parent.trigger.emit(u'第四（3）步开始执行，请稍等...')

    if common.debugOn:
        common.logging.debug(u'/**************第四（3）步****************/')

    cond['step'] = '43'

    tempfilePath = filepath + '\\' + u'第四（3）步'

    if not os.path.exists(tempfilePath):
        os.mkdir(tempfilePath)
    hs.clearResultList()
    hs.four_3_step(tempfilePath, hsrst245, hsrst345, cond)

    if not parent is None:
        parent.trigger.emit(u'第四（3）步执行结束！')
    ####################################################
    ## 第四（4）步
    ####################################################
    if not parent is None:
        parent.trigger.emit(u'第四（4）步开始执行，请稍等...')

    if common.debugOn:
        common.logging.debug(u'/**************第四（4）步****************/')

    cond['step'] = '44'

    tempfilePath = filepath + '\\' + u'第四（4）步'

    if not os.path.exists(tempfilePath):
        os.mkdir(tempfilePath)
    hs.clearResultList()
    hs.four_4_step(tempfilePath, pmrst145,hsrst245, hsrst345, cond)

    if not parent is None:
        parent.trigger.emit(u'第四（4）步执行结束！')

    ####################################################
    ## 第四（5）步
    ####################################################
    if not parent is None:
        parent.trigger.emit(u'第四（5）步开始执行，请稍等...')

    if common.debugOn:
        common.logging.debug(u'/**************第四（5）步****************/')

    cond['step'] = '45'

    tempfilePath = filepath + '\\' + u'第四（5）步'

    if not os.path.exists(tempfilePath):
        os.mkdir(tempfilePath)
    hs.clearResultList()
    hs.four_57_step(tempfilePath, pmrst1, '5')

    if not parent is None:
        parent.trigger.emit(u'第四（5）步执行结束！')

    ####################################################
    ## 第四（6）步
    ####################################################
    if not parent is None:
        parent.trigger.emit(u'第四（6）步开始执行，请稍等...')

    if common.debugOn:
        common.logging.debug(u'/**************第四（6）步****************/')

    cond['step'] = '46'

    tempfilePath = filepath + '\\' + u'第四（6）步'

    if not os.path.exists(tempfilePath):
        os.mkdir(tempfilePath)
    hs.clearResultList()
    hs.four_68_step(tempfilePath, pmrst1, '6')

    if not parent is None:
        parent.trigger.emit(u'第四（6）步执行结束！')

    ####################################################
    ## 第四（7）步
    ####################################################
    if not parent is None:
        parent.trigger.emit(u'第四（7）步开始执行，请稍等...')

    if common.debugOn:
        common.logging.debug(u'/**************第四（7）步****************/')

    cond['step'] = '47'

    tempfilePath = filepath + '\\' + u'第四（7）步'

    if not os.path.exists(tempfilePath):
        os.mkdir(tempfilePath)
    hs.clearResultList()
    hs.four_57_step(tempfilePath, hsrst2, '7')

    if not parent is None:
        parent.trigger.emit(u'第四（7）步执行结束！')

    ####################################################
    ## 第四（8）步
    ####################################################
    if not parent is None:
        parent.trigger.emit(u'第四（8）步开始执行，请稍等...')

    if common.debugOn:
        common.logging.debug(u'/**************第四（8）步****************/')

    cond['step'] = '48'

    tempfilePath = filepath + '\\' + u'第四（8）步'

    if not os.path.exists(tempfilePath):
        os.mkdir(tempfilePath)
    hs.clearResultList()
    hs.four_68_step(tempfilePath, hsrst2, '8')

    if not parent is None:
        parent.trigger.emit(u'第四（8）步执行结束！')

    ####################################################
    ## 统计
    ####################################################
    hs.addcsvDict(pm.getcsvDict())
    hs.statistics(filepath, cond)

if __name__ == '__main__':
    starttime = datetime.now()
    cond = {'num1':'1','num2':'2','num3':'3','num4':'4','error':3,'jhsel':10,'jherr':8,'h2err':9,'h3err':9}
    heshucond = {'ab':'4',
             'ac':'5',
             'ad':'6',
             'bc':'5',
             'bd':'6',
             'cd':'7',
             'abc':'6',
             'abd':'7',
             'acd':'8',
             'bcd':'9',
             'h2err':'2',
             'h3err':'1',
             'h2err2':'14',
             'h3err2':'14','jhsel':10,'jherr':8,
             'step':'22','checknum':'1234'
             }
    #first(cond)
    #first45(cond)
    #second(heshucond, 'F:\\test', None)
    three45(heshucond)
    #three(heshucond)
    endtime = datetime.now()
    tend = endtime - starttime
    print(u'执行时间：'+str(tend.seconds)+u'秒')
