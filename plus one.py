# -*- coding: utf-8 -*-
"""
Created on Wed May 20 13:05:40 2020

@author: rishabhsaxena01
"""

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = True
        idx = len(digits)-1
        
        while carry:
            if idx < 0:
                digits = [1]+digits
                break
            digits[idx] += 1
            if digits[idx] >= 10:
                digits[idx] -= 10
                carry = True
            else:
                carry = False
            
            idx -= 1
        return digits
    

#solution 2
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        res = int("".join(map(str, digits))) 
        res+=1
        return list(map(int, str(res)))


