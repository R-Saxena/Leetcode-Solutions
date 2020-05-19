# -*- coding: utf-8 -*-
"""
Created on Fri May 15 14:52:18 2020

@author: rishabhsaxena01
"""

class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        B = []
        for i in A:
            if i%2==0:
                B.insert(0,i)
            else:
                B.append(i)
        
        return B