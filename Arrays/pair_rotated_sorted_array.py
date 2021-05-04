"""
Given a sorted and rotated array, find if there is a pair with a given sum
Difficulty Level : Medium
Last Updated : 08 Apr, 2021
Given an array that is sorted and then rotated around an unknown point. Find if the array has a pair with a given sum ‘x’.
It may be assumed that all elements in the array are distinct.

Examples :

Input: arr[] = {11, 15, 6, 8, 9, 10}, x = 16
Output: true
There is a pair (6, 10) with sum 16

Input: arr[] = {11, 15, 26, 38, 9, 10}, x = 35
Output: true
There is a pair (26, 9) with sum 35

Input: arr[] = {11, 15, 26, 38, 9, 10}, x = 45
Output: false
There is no pair with sum 45.
"""
arr = [11, 15, 6, 8, 9, 10]
x = 22


# Hashing technique
def findPair(array, sum_):
    hash_map = set()
    for elem in array:
        other_elem = sum_ - elem
        if other_elem in hash_map:
            print("Pair with sum:", (elem, other_elem))
            return 1
        hash_map.add(elem)
    print("No pair with sum", sum_)

ans = findPair(arr, x)


def find_pair_rotated(array, sum_):
    """
    Pseudo-Algorithm:
    1. Identify the largest element, the smallest element would be the one next to it.
    2. Once the smallest element is identified, we can increase the left and right indices using modular arithmetic.
    """
    N = len(array)
    for i in range(len(array)):
        if array[i] > array[i+1]:
            break

    smallest = (i + 1) % N
    largest = i

    while smallest != largest:

        if array[smallest] + array[largest] == sum_:
            return True
        elif array[smallest] + array[largest] < sum_:
            smallest = (smallest + 1) % N
        elif array[smallest] + array[largest] > sum_:
            largest = (N + largest -1) % N

    return False


ans = find_pair_rotated(arr, x)
print(ans)



