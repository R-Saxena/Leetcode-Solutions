# -*- coding: utf-8 -*-
"""
Created on Wed May 20 11:50:12 2020

@author: rishabhsaxena01
"""
class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        maxVal = -1
        secMax = -1
        maxIndex = -1
        for i, n in enumerate(nums):
            if n >= maxVal:
                maxIndex = i
                secMax = maxVal
                maxVal = n
            elif n > secMax:
                secMax = n
        return maxIndex if (maxVal >= 2 * secMax) else -1
    
#solution 2   
class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        x = sorted(nums, reverse = True)
        
        if len(x)==0:
            return -1
        if len(x) == 1:
            return 0
        
        if x[0] >= x[1]*2:
            return nums.index(max(nums))
        else:
            return -1
