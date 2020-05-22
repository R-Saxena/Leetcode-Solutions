# -*- coding: utf-8 -*-
"""
Created on Fri May 22 12:37:11 2020

@author: rishabhsaxena01
"""

class Solution:
    def findDiagonalOrder(self, matrix: List[List[int]]) -> List[int]:
        m = len(matrix)
        n = len(matrix[0]) if m > 0 else 0
        if n==0:
            return []
        
        up = True
        row =0
        col = 0
        res = []
        
        for i in range(m*n):
            res.append(matrix[row][col])

            if up:
                if col == n-1:
                    row = row +1
                    up = not up
                elif row == 0:
                    col = col+1
                    up = not up
                else:
                    row = row-1
                    col = col+1
            else:
                if row == m-1:
                    col +=1
                    up = not up
                elif col == 0:
                    row+=1
                    up = not up
                else:
                    row+=1
                    col-=1
        return res