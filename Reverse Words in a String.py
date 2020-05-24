# -*- coding: utf-8 -*-
"""
Created on Sun May 24 20:26:32 2020

@author: rishabhsaxena01
"""

class Solution:
    def reverseWords(self, s: str) -> str:
        li = s.split()
        li.reverse()
        return " ".join(li)
    
    
    
    
class Solution:
    def reverseWords(self, s: str) -> str:
        arr = s.strip().split(' ')
        arr = [x for x in arr if x !='']
        print(arr)
        i = 0
        j = len(arr) - 1
        while i <= j:
            temp = arr[i]
            arr[i] = arr[j]
            arr[j] = temp
            i += 1
            j -= 1

        output = ' '.join(arr)
        print(len(output))
        print(len(s))
        return output