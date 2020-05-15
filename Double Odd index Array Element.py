# -*- coding: utf-8 -*-
"""
Created on Fri May 15 02:13:08 2020

@author: rishabhsaxena01
"""

arr = [9, -2, -9, 11, 56, -12, -3]
N = len(arr)
i=0
while i <N:
    arr[i] = arr[i]*arr[i]
    i+=2
    
print(arr)