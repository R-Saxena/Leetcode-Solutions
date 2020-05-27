# -*- coding: utf-8 -*-
"""
Created on Wed May 27 21:25:40 2020

@author: rishabhsaxena01
"""

class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        return str(eval(num1 + ' + '+ num2))