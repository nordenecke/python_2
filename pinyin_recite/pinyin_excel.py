# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
source = load_cn_words('e:\文档\自动出题\词语默写.txt')
#shuffle(source)  # 打乱顺序

columns, rows = 15, 11  # 控制每页行列
page_limit = 10  # 控制输出页数
row_cur, page_cur = 1, 1
def generator():
    global source, columns, rows, row_cur, page_cur, page_limit
    if not source or page_cur > page_limit:
        STOP()
    pinyin_lst, hanzi_lst, hanzi_blank_lst = [], [], []
    while True:
        if not source:
            break
        word = source.pop(0)
        word1 = ' ' + word
        hanzi_word = ''
        if len(pinyin_lst) + len(word1) <= columns:
            pinyin_lst += [i[0] for i in pinyin(word1)]
            hanzi_lst += list(word)
            hanzi_word +='('
            j = 0
            while j < len(word):
                hanzi_word += ' '
                j+=1
            hanzi_word += ')'
            hanzi_blank_lst+=list(hanzi_word)
            if len(pinyin_lst) + 1 < columns:
                pinyin_lst.append(' ')
                hanzi_lst.append(' ')
        else:
            source.insert(0, word)
            break
    while len(pinyin_lst) < columns:
        pinyin_lst.append(' ')
        hanzi_lst.append(' ')
    row_cur += 1
    if row_cur > rows:
        row_cur = 1
        page_cur += 1
    # 选择输出内容
    #return pinyin_lst + ['EOL'] + hanzi_lst  # 拼音+汉字
    #return ['EOL'] + hanzi_lst  # 仅汉字
    #return pinyin_lst + ['EOL']  # 仅拼音
    return pinyin_lst + ['EOL'] + ['EOL'] + hanzi_blank_lst + ['EOL']   # 拼音+汉字空格 [老婆要求 :( ]
