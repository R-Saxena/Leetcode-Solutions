# -*- coding: utf-8 -*-
"""
Created on Thu May 14 15:38:49 2020

@author: rishabhsaxena01
"""

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        i = 1
        for j in range(1,len(nums)):
            if nums[j]!=nums[j-1]:
                nums[i] = nums[j]
                i+=1
        
        print(nums)
        return i