# -*- coding: utf-8 -*-
"""
Created on Fri May 29 21:44:48 2020

@author: rishabhsaxena01
"""

li = []
n = int(input())
li = list(map(int, input().split()))
# print(li)

li.sort()
flag = False
for i in range(len(li)-1):
    if li[i+1] - li[i] not in [0,1]:
        flag = True
        break

if flag:
    print('NO')
else:
    print('YES')