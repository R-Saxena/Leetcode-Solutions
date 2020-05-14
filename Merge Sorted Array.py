# -*- coding: utf-8 -*-
"""
Created on Thu May 14 13:46:12 2020

@author: rishabhsaxena01
"""

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        
        for i in range(n):
            nums1[m+i] = nums2[i]
        
        nums1.sort()