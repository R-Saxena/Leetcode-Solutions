# -*- coding: utf-8 -*-
"""
Created on Wed May 13 01:08:22 2020

@author: rishabhsaxena01
"""

class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        for i in range(len(A)):
            A[i] = A[i]*A[i]
        A.sort()
        return A