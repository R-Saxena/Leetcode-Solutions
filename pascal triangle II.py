# -*- coding: utf-8 -*-
"""
Created on Sun May 24 19:59:05 2020

@author: rishabhsaxena01
"""

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        line = rowIndex+1
        result = []
        c=1
        for i in range(1, line+1):
            result.append(c)
            c = int(c*(line-i)/i)
            
        return result