# -*- coding: utf-8 -*-
"""
Created on Wed May 13 01:04:26 2020

@author: rishabhsaxena01
"""

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        
        k=0
        max_k=0
        for i in nums:
            if i==1:
                k = k+1
            else:
                k=0
            
            if max_k < k:
                max_k = k
                
        return max_k