# -*- coding: utf-8 -*-
"""
Created on Fri May 15 01:14:36 2020

@author: rishabhsaxena01
"""

class Solution:
    def validMountainArray(self, A: List[int]) -> bool:
        if len(A) < 3 or A[0] >=A[1] or A[-2] <= A[-1]:
            return False
        flag = True
        for i,j in zip(A,A[1:]):
            if i==j:
                return False
            elif i<j:
                if not flag:
                    return False
            else:
                if flag:
                    flag = False
        return not flag
    
    
#solution 2
class Solution(object):
    def validMountainArray(self, A):
        N = len(A)
        i = 0

        # walk up
        while i+1 < N and A[i] < A[i+1]:
            i += 1

        # peak can't be first or last
        if i == 0 or i == N-1:
            return False

        # walk down
        while i+1 < N and A[i] > A[i+1]:
            i += 1

        return i == N-1