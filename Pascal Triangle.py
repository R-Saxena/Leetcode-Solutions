# -*- coding: utf-8 -*-
"""
Created on Fri May 22 23:00:27 2020

@author: rishabhsaxena01
"""
#solution 1
def check(li,i,j):
    try:
        if j-1 >=0:
            return li[i-1][j-1]+li[i-1][j]
        else:
            return 1
    except:
        return 1

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        li = []
        for i in range(1, numRows+1):
            val = []
            for j in range(i):
                res = check(li, i-1,j)
                val.append(res)
            li.append(val)
        
        return li
    
#solution 2

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        li = []
        for line in range(1, numRows+1):
            c=1
            val = []
            for i in range(1, line+1):
                val.append(c)
                c = int(c*(line - i)/i)
            li.append(val)
        
        return li