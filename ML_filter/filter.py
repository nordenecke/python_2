# -*- coding: utf-8 -*-
"""
Created on Sun Feb 11 22:11:19 2018

@author: eqhuliu
"""

#import subprocess
##import time
#
#p = subprocess.Popen('tail -F data.txt', shell=True, stdout=subprocess.PIPE,stderr=subprocess.PIPE,)
#while True:
#   line = p.stdout.readline()
#   if line:
#        print line

import re

p = 0
with open('data.txt', 'r+') as f:
    with open('output.txt', 'w') as g:
        g.write('Hello, world!')
    while True:
        line = f.readline()
        if line:
            print line
            pattern_1=re.compile("<proto name=\"pgsl\"*?</proto>",re.DOTALL)

            #    print("error word:%s" %word)
            if None==pattern_1.search(line):
                print "Not found2!"
            else:
                result1=pattern_1.search(line).group()
                pattern_2=re.compile('PGSL-ULDATA-IND*?unmaskedvalue')
                if None==pattern_1.search(line):
                    print "Not found2!"
                result2=pattern_2.search(result1).group()

                phonetic_list=[]
                phonetic_str=""
                for j in pattern_2.findall(result):
                    phonetic_list.append(j)
                if len(phonetic_list)>=2:
                    phonetic_str=phonetic_list[1].strip('<span class="phonetic">').strip('</span>')
            #            print(phonetic_str)
