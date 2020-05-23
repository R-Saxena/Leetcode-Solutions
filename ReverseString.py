# -*- coding: utf-8 -*-
"""
Created on Sat May 23 01:43:09 2020

@author: rishabhsaxena01
"""
#solution 1
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        for i in range(len(s)):
            x = s.pop()
            s.insert(i, x)
            # print(s)
            
            
#solution 2
            
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        i = 0
        j = len(s)-1
        while not i>=j:
            s[i],s[j] = s[j],s[i]
            i+=1
            j-=1
            

#solution 3
            
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        def helper(i, j):
            if i < j:
                s[i], s[j] = s[j], s[i]
                helper(i + 1, j - 1)

        helper(0, len(s) - 1)

