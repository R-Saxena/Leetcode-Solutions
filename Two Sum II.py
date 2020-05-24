# -*- coding: utf-8 -*-
"""
Created on Sat May 23 21:35:50 2020

@author: rishabhsaxena01
"""
#solution 1
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        index1 = 0
        index2 = 0
        for i in range(len(numbers)):
            if numbers[i] > target:
                break
            remain = target-numbers[i] 
            if remain in numbers:
                index1 = i+1
                index2 = numbers[i+1:].index(remain) + 1+i+1
                break
                
        return index1,index2
    
#solution 2
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        start = 0
        end = len(numbers)-1
        while start < end:
            su = numbers[start]+numbers[end]
            if su == target:
                return [start+1, end+1]
            elif su < target:
                start+=1
            else:
                end-=1
                
        return [-1,-1]