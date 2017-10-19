# -*- coding: utf-8 -*-
"""
Created on Wed Sep 27 15:08:30 2017

@author: eqhuliu
"""

import numpy as np
import matplotlib.pyplot as plt
x=np.arange(-5, 5, 0.001)
y=x**4-3*x**3+2
plt.plot(x,y)  
plt.show()

x=np.arange(-5, 5, 0.001)
y=4*x**3-9*x**2
plt.plot(x,y)  
plt.show()


old = 0
new= 6 #5 
step = 0.001
precision = 0.000001

def derivative(x):
    return 4*x**3-9*x**2

while abs(new - old) > precision:
    old = new
    print (new)
    new = new - step * derivative(new)

print (new)


