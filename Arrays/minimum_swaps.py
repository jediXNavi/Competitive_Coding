"""
Minimum swaps required to bring all elements less than or equal to k together
Difficulty Level : Medium
Last Updated : 19 Jul, 2018
Given an array of n positive integers and a number k. Find the minimum number of swaps required to bring all the numbers less than or equal to k together.

Input:  arr[] = {2, 1, 5, 6, 3}, k = 3
Output: 1

Explanation:
To bring elements 2, 1, 3 together, swap
element '5' with '3' such that final array
will be-
arr[] = {2, 1, 3, 6, 5}

Input:  arr[] = {2, 7, 9, 5, 8, 7, 4}, k = 5
Output: 2
"""
given = [2, 7, 9, 5, 8, 7, 4]
k = 5


# O(n) time complexity
def minimum_swaps(arr, k, l, r):
    swap = 0
    while r > l:
        if arr[l] <= k < arr[r]:
            l += 1
        elif arr[l] > k and arr[r] > k:
            r -= 1
        elif arr[l] <= k and arr[r] <= k:
            l += 1
        elif arr[r] <= k < arr[l]:
            temp = arr[r]
            arr[r] = arr[l]
            arr[l] = temp
            r -= 1
            l += 1
            swap += 1

    return swap


ans = minimum_swaps(given, k, 0, len(given) - 1)
print(ans)
