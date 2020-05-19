# -*- coding: utf-8 -*-
"""
Created on Tue May 19 05:55:04 2020

@author: rishabhsaxena01
"""

#solution 1
from collections import Counter
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        x = Counter([i for i in range(1, len(nums)+1)])
        y = Counter(nums)
        x.subtract(y)
        return list(x.elements())
    
    
#solution 2
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        return list(set(range(1,len(nums)+1)) - set(nums))