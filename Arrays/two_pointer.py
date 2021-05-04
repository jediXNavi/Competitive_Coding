"""Two Pointer approach for solving problems with arrays

Given a array A and a sum x, find the pair that gives the sum
"""
arr = [2, 6, 24, 9, 51, 100, 45, 32]
target = 30


# Two pointer approach: O(nlogn)
def findPair(array, array_size, sum_):
    ptr_l = 0
    ptr_r = array_size - 1

    array.sort()
    while ptr_l < ptr_r:
        current_sum = array[ptr_l] + array[ptr_r]
        if current_sum > sum_:
            ptr_r -= 1
        elif current_sum < sum_:
            ptr_l += 1
        elif current_sum == sum_:
            return array[ptr_l], array[ptr_r]


ans = findPair(arr, len(arr), target)
print(ans)


# Hashing trick approach: O(1)
# Does not require sorting
def findPair_2(array, sum_):
    hash_map = set()
    for elem in array:
        other_elem = sum_ - elem
        if other_elem in hash_map:
            return elem, other_elem
        hash_map.add(elem)


ans = findPair_2(arr, target)
print(ans)
