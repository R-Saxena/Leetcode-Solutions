# -*- coding: utf-8 -*-
"""
Created on Wed May 13 23:23:24 2020

@author: rishabhsaxena01
"""

class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        li = []
        n = len(arr)
        for i in range(n):
            if arr[i]==0:
                li.append(i)
    
        for i in range(len(li)):
            arr.insert(li[i]+i,0)
            arr.pop()