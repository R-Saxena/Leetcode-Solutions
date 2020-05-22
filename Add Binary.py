# -*- coding: utf-8 -*-
"""
Created on Fri May 22 17:01:46 2020

@author: rishabhsaxena01
"""

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        return bin(int(a,2)+int(b,2))[2:]