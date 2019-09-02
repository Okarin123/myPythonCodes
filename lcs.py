#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 24 17:54:07 2019

@author: amogh
"""

strOne = str(input()) 
strTwo = str(input())
m = len(strOne) 
n = len(strTwo) 

lcs = [[0 for x in range (n+1)] for x in range (m+1)] 

for i in range (m+1): 
    for j in range (n+1): 
        if i==0 or j==0: 
            lcs[i][j] = 0
        elif strOne[i-1] == strTwo[j-1]: 
            lcs[i][j] = 1+lcs[i-1][j-1]
        else: 
            lcs[i][j] = max(lcs[i-1][j], lcs[i][j-1]) 
    
finalAns = ''
i = m
j = n
while i>0:
    if lcs[i][j] == lcs[i-1][j]+1: 
        finalAns = finalAns + str(strOne[i-1])
        i -= 1
        j -= 1
    else: 
        i -= 1

finalAns = finalAns[::-1] 
print("Longest common subsequence is", finalAns) 
print("Length = ", len(finalAns))