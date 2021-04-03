'''
Find the first occurrence of a number greater than k
in a sorted array.

Example...

If the input array is [2, 20, 30] and k is 3, then return index 1: 20

'''

def greaterThanK(arr, k):
    for index in range(len(arr)):
        if arr[index] > k:
            return index


arr = [2, 20, 30]
print(greaterThanK(arr, 3))
