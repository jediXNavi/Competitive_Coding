"""
Binary search is an efficient searching algorithm that searches an element in an array in O(logn) time.
It assumes that the array or list is sorted.

Steps for binary search:
==================================================
1. Identify the middle element.
2. If middle element is less than the search item, use the array greater than the middle item to search.
3. Repeat the same steps over and over until we get the index of the search item or nothing.
"""
import math


def binary_search(arr, search_key, l, r):
    print(arr)
    if r >= l:
        # To find the middle element and avoid overflow? Reason is not exactly clear to me but yea.
        mid = l + (r - l) // 2
        middle_elem = arr[mid]
        if middle_elem > search_key:
            return binary_search(arr, search_key, l, mid-1)
        elif middle_elem < search_key:
            return binary_search(arr, search_key, mid + 1, r)
        elif middle_elem == search_key:
            return mid
    else:
        return "Does not exist"


que_arr = [1, 2, 3, 4, 55, 67]
ans = binary_search(que_arr, 67, 0, len(que_arr)-1)
print(ans)
