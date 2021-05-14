"""
Reorder an array according to given indexes
Difficulty Level : Medium
Last Updated : 05 May, 2021
Given two integer arrays of same size, “arr[]” and “index[]”, reorder elements in “arr[]” according to given index array. It is not allowed to given array arr’s length.

Example:

Input:  arr[]   = [10, 11, 12];
        index[] = [1, 0, 2];
Output: arr[]   = [11, 10, 12]
        index[] = [0,  1,  2]

Input:  arr[]   = [50, 40, 70, 60, 90]
        index[] = [3,  0,  4,  1,  2]
Output: arr[]   = [40, 60, 90, 50, 70]
        index[] = [0,  1,  2,  3,   4]
Expected time complexity O(n) and auxiliary space O(1)
"""
given = [50, 40, 70, 60, 90]
index = [3,  0,  4,  1,  2]


def reorder_array(arr, index_arr):
    temp = [0] * len(arr)
    ind_arr = []
    for ind_, i in enumerate(range(len(temp))):
        temp[index_arr[i]] = arr[i]
        ind_arr.append(ind_)

    return temp, ind_arr

print(reorder_array(given, index))
