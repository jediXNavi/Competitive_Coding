"""
Rearrange positive and negative numbers with constant extra space
Difficulty Level : Medium
Last Updated : 05 May, 2021
Given an array of positive and negative numbers, arrange them such that all negative integers appear before all the
positive integers in the array without using any additional data structure like hash table, arrays, etc.
The order of appearance should be maintained.

Examples:

Input:  [12 11 -13 -5 6 -7 5 -3 -6]
Output: [-13 -5 -7 -3 -6 12 11 6 5]
"""
given = [12, 11, -13, -5, 6, -7, 5, -3, -6]


# Modified insertion sort
def rearrange_pos_negative_numbers(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        # Predecessor element
        j = i - 1
        while j >= 0 and arr[j] > 0:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key

    return arr


print(rearrange_pos_negative_numbers(given))