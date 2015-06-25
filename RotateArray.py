'''
Rotate an array of n elements to the right by k steps.

For example, with n = 7 and k = 3, the array [1,2,3,4,5,6,7] is rotated to [5,6,7,1,2,3,4].
'''

'''
The idea of this solution is: the array we can cut it into 2, A:[1,2,3,4,5] B:[6,7].
To get the result[B,A], first revers A, then reverse B, then reverse the entire array.
The time complexity is O(n) and space complexity is O(1)
'''

class Solution:
    # @param {integer[]} nums
    # @param {integer} k
    # @return {void} Do not return anything, modify nums in-place instead.
    def rotate(self, nums, k):
        length = len(nums)
            
        if k == 0 or k == length:
            return
        if k < 0:
            return None
        if k > length:
            k = k % length
        
        self.reverse(nums, 0, length - 1 - k)
        self.reverse(nums, length - k, length - 1)
        self.reverse(nums, 0, length - 1)
        
    
    def reverse(self, myList, start, end):
        tmp = 0
        while start < end:
            tmp = myList[start]
            myList[start] = myList[end]
            myList[end] = tmp
            start += 1
            end -= 1
