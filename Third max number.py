# -*- coding: utf-8 -*-
"""
Created on Fri May 15 14:58:41 2020

@author: rishabhsaxena01
"""
#solution 1

class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        nums = list(set(nums))
        if len(nums) > 2:
            return sorted(nums)[-3]
        else:
            return max(nums)








#solution 2
f = s = t = float("-inf")
        
        for e in nums:
            if e == f or e == s or e == t:
                continue
            
            if e > f:
                f, s, t = e, f, s
            elif e > s:
                s, t = e, s
            elif e > t:
                t = e
                
        return t if t != float("-inf") else f