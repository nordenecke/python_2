# -*- coding: utf-8 -*-
"""
Created on Sun Jul  9 21:45:56 2017

@author: norden
"""

#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2014-04-03 21:12:16
# @Function: 有道翻译命令行版
# @Author : BeginMan

#import os
import sys
import urllib
import importlib
importlib.reload(sys)
import simplejson as json
import platform
import datetime

API_KEY = '******'
KEYFORM = '******'

def GetTranslate(txt):
    url = 'http://fanyi.youdao.com/openapi.do'
    data = {
    'keyfrom': KEYFORM,
    'key': API_KEY,
    'type': 'data',
    'doctype': 'json',
    'version': 1.1,
    'q': txt
    }
    data = urllib.parse.urlencode(data)
    url = url+'?'+data
    print(u"url=%s" %(url))
    req = urllib.request.Request(url)
    response = urllib.request.urlopen(req)
    result = json.loads(response.read())
    print(result)
    return result

def Sjson(json_data):
    query = json_data.get('query','')                # 查询的文本
    translation = json_data.get('translation','')    # 翻译
#    print("translation=%s",%(translation))
    print("translation:%s" %(translation))
    basic = json_data.get('basic','')                # basic 列表
    sequence = json_data.get('web',[])             # 短语列表
    phonetic,explains_txt,seq_txt,log_word_explains = '','','',''

    # 更多释义
    if basic:
        phonetic = basic.get('phonetic','')         # 音标
        print("phonetic:%s" %(phonetic))
        explains = basic.get('explains',[])         # 更多释义 列表
        print("explains:%s" %(explains))
        for obj in explains:
            explains_txt += obj+'\n'
            log_word_explains += obj+','
    # 句子解析
    if sequence:
        for obj in sequence:
            seq_txt += obj['key']+'\n'
            values = ''
            for i in obj['value']:
                values += i+','
            seq_txt += values+'\n'

    print_format = '*'*40+'\n'
    print_format += u'查询对象: %s [%s]\n' %(query,phonetic)
    print_format += explains_txt
    print_format += '-'*20+'\n'+seq_txt
    print_format += '*'*40+'\n'
    print(print_format)
    choices = input(u'是否写入单词本,回复（y/n）:')
    if choices in ['y','Y']:
        filepath = r'/home/beginman/pyword/%s.xml' %datetime.date.today()
        if (platform.system()).lower() == 'windows':
            filepath = r'E:\workspace\python\bdc\%s.xml' %datetime.date.today()
        fp = open(filepath,'a+')
        file = fp.readlines()
        if not file:
            fp.write('<wordbook>\n')
            fp.write(u"""    <item>\n    <word>%s</word>\n    <trans><![CDATA[%s]]></trans>\n    <phonetic><![CDATA[[%s]]]></phonetic>\n    <tags>%s</tags>\n    <progress>1</progress>\n    </item>\n\n""" %(query,log_word_explains,phonetic,datetime.date.today()))
        fp.close()
        print(u'写入成功.')

def main():
    while True:
        txt = input(u'请输入要查询的文本：\n')
        if txt!="quit":
            Sjson(GetTranslate(txt))
        else:
            break

if __name__ == '__main__':
    main()