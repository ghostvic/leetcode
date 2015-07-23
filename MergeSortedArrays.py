'''
Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.
Note:
You may assume that nums1 has enough space (size that is greater or equal to m + n) to hold additional elements 
from nums2. The number of elements initialized in nums1 and nums2 are m and n respectively.
'''

'''
In this solution, we assume that both the 2 arrays are sorted in ascending order.
Some points:
A. Do not forget to deal with the elements after one array is finished.
B. nums[0] is valid, so the consider should be greater than -1 
And the time complexity is O(m+n)
'''

class Solution:
    # @param {integer[]} nums1
    # @param {integer} m
    # @param {integer[]} nums2
    # @param {integer} n
    # @return {void} Do not return anything, modify nums1 in-place instead.
    def merge(self, nums1, m, nums2, n):
        (i, j) = (m-1, n-1)
        timeOfMove = 0
        while j > -1 and i > -1:
            if nums2[j] > nums1[i]:
                nums1[m + n - timeOfMove - 1] = nums2[j]
                j -= 1
            else:
                nums1[m + n - timeOfMove - 1] = nums1[i]
                i -= 1
            timeOfMove += 1
            
        if j > -1:
            nums1[:j+1] = nums2[:j+1]
