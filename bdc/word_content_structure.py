# -*- coding: utf-8 -*-
"""
Created on Sat Jul 15 22:36:23 2017

@author: norden
"""

class word_content(object):
    def __init__(self,word,phonetic_symbol,paraphrase):
        self.word=word
        self.phonetic_symbol=phonetic_symbol
        self.paraphrase=paraphrase

#wc=word_content("xxx","yyy","zzz")
#print(wc.word)