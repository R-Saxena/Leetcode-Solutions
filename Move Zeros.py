# -*- coding: utf-8 -*-
"""
Created on Fri May 15 02:34:53 2020

@author: rishabhsaxena01
"""
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        non_zero_index = 0
        for i in range(len(nums)):
            if nums[i]!=0:
                nums[non_zero_index] = nums[i]
                non_zero_index+=1
        
        for i in range(non_zero_index, len(nums)):
            nums[i] =0