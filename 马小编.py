#!/usr/bin/python
# -*- coding: UTF-8 -*-
import os, re, sys, io
import win32_unicode_argv
import json
import getopt
reload(sys)
sys.setdefaultencoding('utf-8')

jsonFileName = 'data.json'

def printUsage():
    print('''usage: 马小编.py -a <主体> -b <事件> -c <别名>''')

def readJson(fileName):
    if fileName != '':
        strList = fileName.split(".")
        if strList[len(strList)-1].lower() == "json":
            with io.open(fileName, mode='r', encoding="utf-8") as file:
                return json.loads(file.read())

if __name__ == "__main__":
    aa = bb = cc = ''
    try:
        opts, args = getopt.getopt(sys.argv[1:], 'ha:b:c:', ['help', 'aa=', 'bb=', 'cc='])
    except getopt.GetoptError:
        printUsage()
        sys.exit(-1)
    if len(opts) != 3:
        printUsage()
        sys.exit(-1)   
    for opt, arg in opts:
        if opt in ('-h', '--help'):
            printUsage()
            sys.exit(-1)
        elif opt in ('-a', '--aa'):
            aa = arg
        elif opt in ('-b', '--bb'):
            bb = arg
        elif opt in ('-c', '--cc'):
            cc = arg
    jsonData = readJson(jsonFileName)
    text = jsonData["text1"]
    text = text.replace('a', aa.encode("utf-8"))
    text = text.replace('b', bb.encode("utf-8"))
    text = text.replace('c', cc.encode("utf-8"))

    print(text)