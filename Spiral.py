# -*- coding: utf-8 -*-
"""
Created on Sat May 23 00:41:18 2020

@author: rishabhsaxena01
"""

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix: return []
        
        ans = []
        
        rows = len(matrix)
        cols = len(matrix[0])
        total = ( rows * cols )
        
        dirs = [ [0,1], [1,0], [0,-1], [-1,0] ]
        mem = set()
        
        i = j = k = 0
        
        while True:
            if len(mem) == total: break
            
            ans.append( matrix[i][j] )
            
            mem.add( (i,j) )
            
            row = i + dirs[k][0]
            col = j + dirs[k][1]
            
            if (row, col) in mem or row<0 or col<0 or row>=rows or col>=cols:
                k = ( k + 1 ) % len(dirs)
                
                i += dirs[k][0]
                j += dirs[k][1]
            else:
                i = row
                j = col
        
        return ans
    
    
    
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        n = len(matrix)
        m = len(matrix[0]) if n > 0 else 0
        if n == 0:
            return []
        
        up = 0
        left = 0
        right = 0
        down = 0

        r_flag = True
        d_flag = False
        u_flag = False
        l_flag = False

        row=0
        col=0

        res= []
        for i in range(n*m):
            res.append(matrix[row][col])

            if u_flag:
                if row == 0+up:
                    col += 1
                    u_flag = not u_flag
                    r_flag = not r_flag
                    left += 1
                else:
                    row -= 1


            elif l_flag:
                if col == 0 + left:
                    row -= 1
                    l_flag = not l_flag
                    u_flag = not u_flag
                    down += 1
                else:
                    col -= 1

            elif d_flag:
                if row == n - down - 1:
                    d_flag = not d_flag
                    l_flag = not l_flag
                    col -= 1
                    right += 1
                else:
                    row += 1


            elif r_flag:
                if col == m - right - 1:
                    row += 1
                    r_flag = not r_flag
                    d_flag = not d_flag
                    up += 1
                else:
                    col += 1     
        
        return res
                