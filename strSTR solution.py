# -*- coding: utf-8 -*-
"""
Created on Fri May 22 17:19:08 2020

@author: rishabhsaxena01
"""

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle) == 0:
            return 0
        
        try:
            return haystack.index(needle)
        except:
            return -1