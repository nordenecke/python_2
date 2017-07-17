# -*- coding: utf-8 -*-
"""
Created on Sun Jul  9 22:00:39 2017

@author: norden
"""

import re
import urllib
#import word_list
import word_content_structure
#print(word_list.get_word_list("words.txt"))

#word=input('input a word\n')
#word="test"
def word2content(word):
    url='http://dict.youdao.com/search?q=%s'%word

    content=urllib.request.urlopen(url)

    pattern=re.compile("<h2.*?</ul>",re.DOTALL)
    content_text=content.read().decode('utf-8')

    print("error word:%s" %word)
    result=pattern.search(content_text).group()
    pattern2=re.compile('<li>.*?</li>')
    pattern3=re.compile('<span class=\"phonetic\">.*?</span>')

    word_str=""
    count=0
    for i in pattern2.findall(result):
        w_l=i.strip('<li>').strip('</li>')
#        print(w_l)
        word_str+=w_l+"\n"
        count+=1
        if count>=3:
            break

    phonetic_list=[]
    phonetic_str=""
    for j in pattern3.findall(result):
        phonetic_list.append(j)
    if len(phonetic_list)>=2:
        phonetic_str=phonetic_list[1].strip('<span class="phonetic">').strip('</span>')
#        print(phonetic_str)
    wc=word_content_structure.word_content(word,phonetic_str,word_str)
    return wc
#add comments for test