# -*- coding: utf-8 -*-
"""
Created on Sat May 30 02:05:12 2020

@author: rishabhsaxena01
"""

class Solution:
    def addDigits(self, num: int) -> int:
        while True:
            sum = 0
            for i in str(num):
                sum+=int(i)
            num = sum
            if sum <10:
                break
        
        return num