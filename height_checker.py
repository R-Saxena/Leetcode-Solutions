# -*- coding: utf-8 -*-
"""
Created on Fri May 15 17:23:32 2020

@author: rishabhsaxena01
"""
class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        sorted_heights = sorted(heights)
        count = 0
        for i in range(len(heights)):
            if sorted_heights[i] != heights[i]:
                count+=1
        return count
