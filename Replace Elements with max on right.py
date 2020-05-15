# -*- coding: utf-8 -*-
"""
Created on Fri May 15 02:24:11 2020

@author: rishabhsaxena01
"""

class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        max_ = arr[-1]
        arr[-1] = -1
        for i in range(len(arr)-2, -1,-1):
            temp = arr[i]
            arr[i] = max_
            if max_ < temp:
                max_ = temp
        arr[-1] = -1
        return arr