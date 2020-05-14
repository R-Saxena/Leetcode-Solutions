# -*- coding: utf-8 -*-
"""
Created on Thu May 14 13:46:50 2020

@author: rishabhsaxena01
"""
#solution 1
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        try:
            while True:
                nums.remove(val)
        except:
            return len(nums)
        
        
#solution 2
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0
        for j in range(len(nums)):
            if nums[j] != val:
                nums[i] = nums[j]
                i += 1
        return i