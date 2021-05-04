"""
How to count all pairs having sum x?
Input: arr[] = {11, 15, 5, 8, 9, 10}, x = 20
Output: 2
There are 2 pairs (11, 9), (15,5) with sum 20.
"""

arr = [11, 15, 5, 8, 9, 10]
x = 20


# def findNumberOfPairs(array, sum_):
#     N = len(array)
#     count = 0
#     for i in range(N):
#         if array[i] > array[i + 1]:
#             break
#
#     s = (i + 1) % N
#     l = i
#
#     while l!=s:
#
#         if array[s] + array[l] == sum_:
#             count += 1
#
#             if s == (l - 1 + N) % N:
#                 return count
#             s = (s + 1) % N
#             l = (l - 1 + N) % N
#
#         elif array[s] + array[l] > sum_:
#             l = (N + l - 1) % N
#         elif array[s] + array[l] < sum_:
#             s = (s + 1) % N
#
#     return count
#
# ans = findNumberOfPairs(arr, x)
# print(ans)



