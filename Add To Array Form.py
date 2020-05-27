# -*- coding: utf-8 -*-
"""
Created on Wed May 27 21:23:57 2020

@author: rishabhsaxena01
"""
#solution 1
class Solution:
    def addToArrayForm(self, A: List[int], K: int) -> List[int]:
        A = list(map(str, A))
        k = int(''.join(A))+K
        ans = list(str(k))
        ans = list(map(int, ans))
        return ans
    
#solution 2
class Solution:
    def addToArrayForm(self, A: List[int], K: int) -> List[int]:
        x = ''
        for i in A:
            x += str(i)
        
        k = int(x)+ K
        ans = []
        for i in str(k):
            ans.append(int(i))
            
        return ans