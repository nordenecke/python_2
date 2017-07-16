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
    with open(filename,"r") as words_src:
        for line in words_src:
            words_list.append(line.strip())
#            print(line.strip())
#        print(words_list)
        return words_list

def put_content(filename, content_list):
    with open(filename,"w+") as content_dst:
        content_dst.truncate()
        for i in range(len(content_list)):
            content_dst.write(content_list[i].word+"\n")
            content_dst.write(content_list[i].phonetic_symbol+"\n")
            content_dst.write(content_list[i].paraphrase+"\n")
            content_dst.write("***************************\n")
        return True



if __name__=="__main__":
    main()