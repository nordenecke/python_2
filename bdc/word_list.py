# -*- coding: utf-8 -*-
"""
Created on Sat Jul 15 21:58:21 2017

@author: norden
"""
import word_content

words_list=[]

c_lst=[]

def main():
    print("This is get_word_list main function!")
    print(get_word_list("words.txt"))
    c_lst.append(word_content.word_content("111","bbb","ccc"))
    c_lst.append(word_content.word_content("222","bbb","ccc"))
    put_content("words_content.txt",c_lst)


def get_word_list(filename):
    with open(filename,"rb") as words_src:
        for line in words_src:
            words_list.append(line.strip())
#            print(line.strip())
#        print(words_list)
        return words_list

def put_content(filename, content_list):
    with open(filename,"wb+") as content_dst:
        content_dst.truncate()
        for i in content_list:
            print(i)
            content_dst.write(i.word+"\n")
#            content_dst.write((word_content.word_content)i.phonetic_symbol+"\n")
#            content_dst.write((word_content.word_content)i.paraphrase+"\n")
#            content_dst.write("***************************")

        return True



if __name__=="__main__":
    main()