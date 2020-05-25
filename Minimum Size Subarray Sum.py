# -*- coding: utf-8 -*-
"""
Created on Mon May 25 02:46:05 2020

@author: rishabhsaxena01
"""

class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        n = len(nums)
        ans = float('inf')
        left = 0
        sum = 0
        for i in range(n):
            sum +=nums[i]
            while(sum >= s):
                ans = min(ans, i+1-left)
                sum -= nums[left]
                left+=1
        
        if ans == float('inf'):
            return 0
        else:
            return ans
            
