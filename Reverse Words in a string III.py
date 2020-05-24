# -*- coding: utf-8 -*-
"""
Created on Sun May 24 20:26:58 2020

@author: rishabhsaxena01
"""

class Solution:
    def reverseWords(self, s: str) -> str:
        if len(s) < 2:
            return s
        li = s.split()
        for i in range(len(li)):
            li[i] = li[i][::-1]
        return " ".join(li)