#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 13 14:49:53 2021

@author: jedixnavi
"""

"""
Question 1:
-------------------
This is a demo task.

Write a function:

def solution(A)

that, given an array A of N integers, returns the smallest positive integer (greater than 0) that does not occur in A.

For example, given A = [1, 3, 6, 4, 1, 2], the function should return 5.

Given A = [1, 2, 3], the function should return 4.

Given A = [−1, −3], the function should return 1.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [1..100,000];
each element of array A is an integer within the range [−1,000,000..1,000,000].
"""
#If all are negative, it should return 1

def solution(A):
    A.sort() #nlogn
    min_value = 1 #O(1)
    for value in A: #O(N)
        if value == min_value and value >0:
            min_value +=1
    
    return min_value
            
A = [-1,-3]
answer = solution(A)
print(answer)