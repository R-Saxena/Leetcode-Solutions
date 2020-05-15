# -*- coding: utf-8 -*-
"""
Created on Thu May 14 16:06:25 2020

@author: rishabhsaxena01
"""

class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        d = {}
        for val in arr:
            if val*2 in d:
                return True
            if val%2 == 0:
                if val/2 in d:
                    return True 
                
            d[val] = val
        return False
    
    