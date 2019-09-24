# -*- coding: utf-8 -*-
"""
Created on Mon Jun  3 19:01:59 2019

@author: Administrator
"""

# IF ELSE Statement

x=10
if x > 1:
    print ("condition 1")
elif x <-1:
    print ("condition 1.5")
else:
    print ("condition 2")
    

# Function

def Pos_or_Neg(x):
    if x>0:
        return ("Positive")
    elif x<0:
        return ("Negative")
    else:
        return ("Zero")
        
# Loops
        
mylist = [1,2,3,4,5]
for i in mylist:
    print(i)
    
    
import math as m
m.sqrt(16)

# help(math.sqrt)


# common method
# .append  .remove     .extend    .index    .sort     .replace(a, b)    