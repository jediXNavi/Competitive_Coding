"""
Given an array, cyclically rotate the array clockwise by one.
Examples:


Input:  arr[] = {1, 2, 3, 4, 5}
Output: arr[] = {5, 1, 2, 3, 4}
"""



def cyclic_rotation(arr):

    last_val = arr.pop()
    arr.insert(0, last_val)

    return arr


ans = cyclic_rotation(arr=[1, 2, 3, 4, 5])
print(ans)