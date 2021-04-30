#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 13 14:49:53 2021

@author: jedixnavi
"""
from data_structures import Stack

# Balancing Paranthesis
def paranthesis_checker(string):
    stack = Stack()
    balanced = True
    index = 0
    while index < len(string) and balanced:
        symbol = string[index]
        if symbol == '(':
            stack.push(symbol)
        else:
            if stack.isEmpty():
                balanced = False
            else:
                stack.pop()
        index = index + 1

    if balanced and stack.isEmpty():
        return True
    else:
        return False

assert paranthesis_checker('((()))') == True, "Failed test of paranthesis"