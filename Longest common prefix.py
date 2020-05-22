# -*- coding: utf-8 -*-
"""
Created on Fri May 22 17:26:05 2020

@author: rishabhsaxena01
"""

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ''
        strs.sort()
        l = min(len(strs[0]), len(strs[-1]))
        i = 0
        while i < l and strs[0][i] == strs[-1][i]:
                i += 1
        return strs[0][:i]
    

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ''
        flag = False
        if len(strs) <1:
            return res
        min_len = min([len(i) for i in strs])
        for i in range(min_len):
            x = strs[0][i]
            for j in strs:
                if j[i] != x:
                    flag = True
                    break
            if not flag:
                res += x
            else:
                break
        
        return res
                    