"""
Insertion Sort
Difficulty Level : Easy
Last Updated : 13 Apr, 2021

Insertion sort is a simple sorting algorithm that works similar to the way you sort playing cards in your hands.
The array is virtually split into a sorted and an unsorted part. Values from the unsorted part are picked and
placed at the correct position in the sorted part.

Algorithm
-----------
To sort an array of size n in ascending order:
1: Iterate from arr[1] to arr[n] over the array.
2: Compare the current element (key) to its predecessor.
3: If the key element is smaller than its predecessor, compare it to the elements before. Move the greater elements one
position up to make space for the swapped element.
"""
given = [-5, 3, 6, 1, 32, 2, 7, 8, 4]

# Time complexity - O(n2)
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key

    return arr


print(insertion_sort(given))
