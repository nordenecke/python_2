# -*- coding: utf-8 -*-
"""
Created on Sun Jul 16 11:48:59 2017

@author: norden
"""
import word_list
import word2content


input_word_list_file=r"words.txt"
output_docx_file=r"wordcard.docx"
word_content_list=[]
def wordcard_generator():
    wl=word_list.get_word_list(input_word_list_file)
#    print(wl)
    for item in wl:
#        print(item)
        word_content=word2content.word2content(item)
#        print(word_content)
        print(word_content.word)
#        print(word_content.phonetic_symbol)
#        print(word_content.paraphrase)
        word_content_list.append(word_content)
#    print(word_content_list)
#    for i in word_content_list:
#        print(i.word)
#        print(i.phonetic_symbol)
#        print(i.paraphrase)
#format/output
    word_list.put_docx(output_docx_file,word_content_list)

def main():
    wordcard_generator()

if __name__=="__main__":
    main()
