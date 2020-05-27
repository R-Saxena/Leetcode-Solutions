# -*- coding: utf-8 -*-
"""
Created on Wed May 27 21:21:00 2020

@author: rishabhsaxena01
"""

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if target == nums[i]+nums[j]:
                    return [i,j]