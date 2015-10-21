#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pandas as pd
import logging
import os
import sys
import numpy as np

debugOn = False

if debugOn:
    logging.basicConfig(level=logging.DEBUG,
                        format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                        datefmt='%a, %d %b %Y %H:%M:%S',
                        filename=r'.\x6.log',
                        filemode='w')


#logging.debug('debug message')
#logging.info('info message')
#logging.warning('warning message')
#logging.error('error message')
#logging.critical('critical message')

numUnames = ['num1', 'num2', 'num3', 'num4', 'ab', 'ac', 'ad', 'bc', 'bd', 'cd', 'abc', 'abd', 'acd', 'bcd']
numUnames2 = ['number', 'ab', 'ac', 'ad', 'bc', 'bd', 'cd', 'abc', 'abd', 'acd', 'bcd']
qxcname = ['a','b','c','d','e','f','g']

gelian = [[0,1,1],
          [1,1,1],
          [0,1,2],
          [1,3,1],
          [0,1,3],
          [0,2,2],
          [1,2,2],
          [0,2,3],
          [0,2,4],
          [1,4,2],
          [0,3,2],
          [0,3,3],
          [1,3,3],
          [0,3,4],
          [1,4,3],
          [0,3,6],
          [1,6,3],
          [0,4,2],
          [0,4,4],
          [1,4,4],
          [0,4,8],
          [1,8,4],
          [0,5,5],
          [1,5,5],
          [1,10,5],
          [0,6,12],
          [1,12,6],
          [0,10,10],
          [1,10,10],
          [1,9,1],
          ]

stepname = {'11':'第一（1）步',
            '12':'第一（2）步',
            '13':'第一（3）步',
            '14':'第一（4）步',
            '21':'第二（1）步',
            '22':'第二（2）步',
            '23':'第二（3）步',
            '24':'第二（4）步',
            '31':'第三（1）步',
            '32':'第三（2）步',
            '33':'第三（3）步',
            '34':'第三（4）步',
            '41':'第四（1）步',
            '42':'第四（2）步',
            '43':'第四（3）步',
            '44':'第四（4）步',
            '45':'第四（5）步',
            '46':'第四（6）步',
            '47':'第四（7）步',
            '48':'第四（8）步',}

def createNumber1Csv():
    nums = np.arange(10000)
    fillNums = [str(x).zfill(4) for x in nums]
    if not os.path.exists(r"C:\vague") :
        os.mkdir(r"C:\vague")
    numfile = open(r"C:\vague\number1.csv","w")
    for num in fillNums:
        listnum = list(num)
        ab = int(listnum[0]) + int(listnum[1])
        ac = int(listnum[0]) + int(listnum[2])
        ad = int(listnum[0]) + int(listnum[3])
        bc = int(listnum[1]) + int(listnum[2])
        bd = int(listnum[1]) + int(listnum[3])
        cd = int(listnum[2]) + int(listnum[3])

        abc = int(listnum[0]) + int(listnum[1]) + int(listnum[2])
        abd = int(listnum[0]) + int(listnum[1]) + int(listnum[3])
        acd = int(listnum[0]) + int(listnum[2]) + int(listnum[3])
        bcd = int(listnum[1]) + int(listnum[2]) + int(listnum[3])

        numfile.write(listnum[0] + ',' + listnum[1] + ',' + listnum[2] + ',' + listnum[3] + ','
                      + str(ab) + ',' + str(ac) + ',' + str(ad) + ',' + str(bc) + ',' + str(bd) + ',' + str(cd) + ','
                      + str(abc) + ',' + str(abd) + ',' + str(acd) + ',' + str(bcd) + '\n')

def createNumber2Csv():
    nums = np.arange(10000)
    fillNums = [str(x).zfill(4) for x in nums]
    if not os.path.exists(r"C:\vague") :
        os.mkdir(r"C:\vague")
    numfile = open(r"C:\vague\number2.csv","w")
    for num in fillNums:
        listnum = list(num)
        ab = int(listnum[0]) + int(listnum[1])
        ac = int(listnum[0]) + int(listnum[2])
        ad = int(listnum[0]) + int(listnum[3])
        bc = int(listnum[1]) + int(listnum[2])
        bd = int(listnum[1]) + int(listnum[3])
        cd = int(listnum[2]) + int(listnum[3])

        abc = int(listnum[0]) + int(listnum[1]) + int(listnum[2])
        abd = int(listnum[0]) + int(listnum[1]) + int(listnum[3])
        acd = int(listnum[0]) + int(listnum[2]) + int(listnum[3])
        bcd = int(listnum[1]) + int(listnum[2]) + int(listnum[3])

        numfile.write(listnum[0] + listnum[1] + listnum[2] + listnum[3] + ','
                      + str(ab) + ',' + str(ac) + ',' + str(ad) + ',' + str(bc) + ',' + str(bd) + ',' + str(cd) + ','
                      + str(abc) + ',' + str(abd) + ',' + str(acd) + ',' + str(bcd) + '\n')

def createqxc():
    nums = np.arange(10000000)
    if not os.path.exists(r"C:\vague") :
        os.mkdir(r"C:\vague")
    numfile = open(r"C:\vague\qxc.csv","w")
    for num in nums:
        listnum = list(str(num).zfill(7))

        numfile.write(listnum[0] + ',' + listnum[1] + ',' + listnum[2] + ',' + listnum[3] + ','
                      + listnum[4] + ',' + listnum[5] + ',' + listnum[6] + '\n')

def getAllAllNum():
    '''
    try:
        #numbers = pd.read_table(r'.\number.dat', sep='::', header=None, names=numUnames)
        numbers = pd.read_csv(r'.\number.csv', header=None, names=numUnames)
    except Exception as err:
        logging.error(err)
    '''
    if not os.path.exists(r"C:\vague\number1.csv") :
        createNumber1Csv()
    numbers = pd.read_csv(r"C:\vague\number1.csv", header=None, names=numUnames)
    return numbers

def getAllAllNum2():
    #numbers = pd.read_table(r'.\number2.dat', sep='::', header=None, names=numUnames2)
    if not os.path.exists(r"C:\vague\number2.csv") :
        createNumber2Csv()
    numbers = pd.read_csv(r"C:\vague\number2.csv", header=None, names=numUnames2)
    return numbers

def getAllqxcNum():
    if not os.path.exists(r"C:\vague\qxc.csv") :
        createqxc()
    numbers = pd.read_csv(r"C:\vague\qxc.csv", header=None, names=qxcname)
    return numbers

if __name__ == '__main__':
    #print(sys.path + ["app"])
    #print(len(getAllAllNum()))
    #a = [1,2,3,4]
    #b = [3,4,5,6]

    #alist = [n for n in range(2, 10 + 1)]
    #print(alist.reverse())
    #print(list(reversed(range(2, 10 + 1))))

    createqxc()
