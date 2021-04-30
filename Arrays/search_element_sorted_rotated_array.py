"""
Search an element in a sorted and rotated array
Difficulty Level : Medium
Last Updated : 16 Apr, 2021

An element in a sorted array can be found in O(log n) time via binary search.
But suppose we rotate an ascending order sorted array at some pivot unknown to you beforehand.
So for instance, 1 2 3 4 5 might become 3 4 5 1 2.

Devise a way to find an element in the rotated array in O(log n) time.
"""


def rotated_binary_search(arr, low, high, search_key):
    if low > high:
        return -1

    mid = (low + high) // 2

    if arr[mid] == search_key:
        return mid

    if arr[high] >= arr[mid]:  # Check for sorted half
        if arr[mid] <= search_key <= arr[high]:  # Check if our desired value lies in the range.
            return rotated_binary_search(arr, mid + 1, high, search_key)
        return rotated_binary_search(arr, low, mid - 1, search_key)

    elif arr[low] <= arr[mid]:  # Check for sorted half
        if arr[low] <= search_key <= arr[mid]:
            return rotated_binary_search(arr, low, mid - 1, search_key)
        return rotated_binary_search(arr, mid + 1, high, search_key)


arr_que = [3, 4, 5, 1, 2]
ans = rotated_binary_search(arr_que, 0, len(arr_que) - 1, 2)
print(ans)
