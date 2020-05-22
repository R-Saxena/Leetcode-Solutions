# -*- coding: utf-8 -*-
"""
Created on Thu May 21 00:52:54 2020

@author: rishabhsaxena01
"""

class Solution:
    """
    @param nums: a list of integer
    @return: return a integer, denote  the maximum number of consecutive 1s
    """
    def findMaxConsecutiveOnes(self, nums):
        current = 0
        count = 0
        res = 0
        
        for i in range(len(nums)):
            count+=1
            
            if nums[i] == 0:
                current = count
                count = 0
                
            if res < current+count:
                res = current + count
        
        return res