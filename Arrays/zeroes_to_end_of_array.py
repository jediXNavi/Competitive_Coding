"""
Move all zeroes to end of array
Difficulty Level : Easy
Last Updated : 18 Mar, 2021
Given an array of random numbers, Push all the zero’s of a given array to the end of the array. For example, if the given arrays is {1, 9, 8, 4, 0, 0, 2, 7, 0, 6, 0}, it should be changed to {1, 9, 8, 4, 2, 7, 6, 0, 0, 0, 0}. The order of all other elements should be same. Expected time complexity is O(n) and extra space is O(1).
Example:


Input :  arr[] = {1, 2, 0, 4, 3, 0, 5, 0};
Output : arr[] = {1, 2, 4, 3, 5, 0, 0};

Input : arr[]  = {1, 2, 0, 0, 0, 3, 6};
Output : arr[] = {1, 2, 3, 6, 0, 0, 0};
"""

def move_zeroes(arr):
    non_zero_count = 0
    arr_len = len(arr)

    # O(n) time complexity and O(1)
    for i in range(arr_len):
        if arr[i] != 0:
            arr[non_zero_count] = arr[i]
            non_zero_count += 1
    while non_zero_count < arr_len:
        arr[non_zero_count] = 0
        non_zero_count += 1

    return arr


array = [1, 2, 0, 4, 3, 0, 5, 0]
ans = move_zeroes(array)
print(ans)
