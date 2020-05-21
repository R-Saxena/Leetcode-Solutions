# -*- coding: utf-8 -*-
"""
Created on Wed May 20 11:29:35 2020

@author: rishabhsaxena01
"""
#solution 1
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return -1
        
        sum_num = [sum(nums[:i]) for i in range(len(nums)+1)]
        
        
        for i in range(1, len(nums)+1):
            if sum_num[i-1] == (sum_num[-1] - sum_num[i]):
                return i-1
        return -1
    
    
#solution 2
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        S = sum(nums)
        leftsum = 0
        for index,value in enumerate(nums):
            if leftsum == (S-value-leftsum):
                return index
            leftsum += value
        
        return -1
    
#solution 3
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        s = sum(nums)
        runningSum = 0
        for i, n in enumerate(nums):
            if s - n == 2 * runningSum:
                return i
            runningSum += n
        return -1
