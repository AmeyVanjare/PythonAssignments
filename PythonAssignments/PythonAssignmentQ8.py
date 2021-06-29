# -*- coding: utf-8 -*-
"""
Created on Tue Jun 29 22:19:00 2021

@author: ameyv
"""

lst=['dxz','axz','bat','rat','cat','pat','bbc','bbm','cbm']
print('original list ',lst)
n=int(input('How many elements u want to enter'))
for i in range(0,n):
    ele=input("enter a string : ")
    for i in reversed(lst):
        if ele[1]==lst[lst.index(i)][1]:
            pos=lst.index(i)
            lst.insert(pos+1, ele)
            break
print(lst)   