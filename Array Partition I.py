# -*- coding: utf-8 -*-
"""
Created on Sat May 23 02:13:21 2020

@author: rishabhsaxena01
"""

class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        max_sum = 0
        for i in range(len(nums)):
            if i % 2 ==0:
                max_sum += nums[i]
        
        return max_sum