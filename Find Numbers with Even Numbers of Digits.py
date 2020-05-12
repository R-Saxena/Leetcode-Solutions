# -*- coding: utf-8 -*-
"""
Created on Wed May 13 01:05:39 2020

@author: rishabhsaxena01
"""
#solution 1
class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        s=0
        for i in nums:
            if len(str(i))%2==0:
                s+=1
        
        return s
    
#solution 2
class Solution:
    def digit(self, n):
        if n == 0:
            return 0
        return 1+self.digit(int(n/10))
    def findNumbers(self, nums: List[int]) -> int:
        s=0
        for i in nums:
            if self.digit(i)%2==0:
                s+=1
        
        return s