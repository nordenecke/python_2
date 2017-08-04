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
    phonetic_str=""
    word_str=""

    url='http://dict.youdao.com/search?q=%s'%word

    content=urllib.urlopen(url)

    content_text=content.read().decode('utf-8')
    pattern_phonetic=re.compile("<h2.*?</h2>",re.DOTALL)

#    print("error word:%s" %word)
    if None==pattern_phonetic.search(content_text):
        phonetic_str=""
    else:
        result=pattern_phonetic.search(content_text).group()
        pattern_phonetic2=re.compile('<span class=\"phonetic\">.*?</span>')
        phonetic_list=[]
        phonetic_str=""
        for j in pattern_phonetic2.findall(result):
            phonetic_list.append(j)
        if len(phonetic_list)>=2:
            phonetic_str=phonetic_list[1].strip('<span class="phonetic">').strip('</span>')
#            print(phonetic_str)

    pattern_word_str=re.compile("<div class=\"trans-container\">.*?</div>",re.DOTALL)
    if None==pattern_word_str.search(content_text):
        word_str=""
    else:
        result=pattern_word_str.search(content_text).group()

        pattern_word_str2=re.compile('<li>.*?</li>')
        pattern_word_str3=re.compile('<p>.*?</p>')
        if []!=pattern_word_str2.findall(result):
            word_str=""
            count=0
            for i in pattern_word_str2.findall(result):
                w_l=i.strip('<li>').strip('</li>')
#                print(w_l)
                word_str+=w_l+"\n"
                count+=1
                if count>=3:
                    break
        elif []!=pattern_word_str3.findall(result):
            word_str=""
            count=0

            for i in pattern_word_str3.findall(result):
                w_l=i.strip('<p>').strip('</p>')
                if count==1:
                    word_str+=w_l+"\n"
                    break
                count+=1
                if count>=2:
                    break
        else:
            word_str=""


    wc=word_content_structure.word_content(word,phonetic_str,word_str)
    return wc
#add comments for test