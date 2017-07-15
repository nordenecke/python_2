# -*- coding: utf-8 -*-
"""
Created on Wed Jul 12 23:00:12 2017

@author: norden
"""

def is_prime(x):
    if(x==0 or x==1):
        return False
    if(x==2):
        return True
    if(x<0):
        return False
    num=x
    for i in range(1,x-1):
        print("i=%d" %i)
        if ((num/(float)(i+1))%1==0):
            print("return false")
            return False
    else:
        print("return true")
        return True

print(is_prime(5))