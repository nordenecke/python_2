# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import os

#import pypinyin
#from pypinyin import pinyin, lazy_pinyin
from pypinyin import pinyin

###############################################################################

class AssertError(Exception):
    pass

class StopError(Exception):
    pass


def ASSERT(condition):
    if not condition:
        raise AssertError()

def STOP(message=''):
    raise StopError(message)
    
def load_cn_words(fname):
    ret=[]
    print 'Chinese file path='+fname
    if not os.path.isfile(fname):
        STOP('file %s not exist!'% fname)
    for l in open(fname,'r').read().decode(encoding='utf8').splitlines():
        l = l.split('#')[0].strip()
        if not l or l == '\ufeff':
            continue
        for w in l.split(' '):
            if not w or w.startswith('~'):
                continue
            if w in ret:
                continue
            ret.append(w)
    return ret

###############################################################################
import _winreg
def get_desktop():
    key = _winreg.OpenKey(_winreg.HKEY_CURRENT_USER,\
                          r'Software\Microsoft\Windows\CurrentVersion\Explorer\Shell Folders',)
    return _winreg.QueryValueEx(key, "Desktop")[0]


def get_cn_word_file_path(filename):
    desktop_path=get_desktop()
    file_path = desktop_path+"\\"+filename
    return file_path
###############################################################################

def generator(source):
    if not source:
        STOP()
    pinyin_lst = []
    hanzi_lst = []
    while True:
        if not source:
            break
        word = source.pop(0)
        print 'Word='+word+'\n'
        pinyin_lst += [i[0] for i in pinyin(word)]
        hanzi_lst += word
    # 选择输出内容
    #return pinyin_lst + ['EOL'] + hanzi_lst  # 拼音+汉字
    #return ['EOL'] + hanzi_lst  # 仅汉字
    #return pinyin_lst + ['EOL']  # 仅拼音
    print 'pinyin_lst=\n'
    print pinyin_lst
    print 'hanzi_lst=\n'
    print hanzi_lst
    return pinyin_lst + ['EOL'] + hanzi_lst + ['EOL']   # 拼音+汉字空格 [老婆要求 :( ]


def pinyin_generator():
    source = load_cn_words(get_cn_word_file_path(u'Chinese_words.txt'))
    print source
    
    columns, rows = 15, 11  # 控制每页行列
    page_limit = 20  # 控制输出页数
    generator(source)


def main():
    pinyin_generator()

if __name__=="__main__":
    main()
