'''
Given an array and a value, remove all instances of that value in place and return the new length.

The order of elements can be changed. It doesn't matter what you leave beyond the new length.
'''

'''
This question is just the same like , I deleted the element, and moved the following elements to this position. 
I used a var length to measure the length and track where I should put the elements.
The time complexity is O(n)
'''

class Solution:
    # @param {integer[]} nums
    # @param {integer} val
    # @return {integer}
    def removeElement(self, nums, val):
        index = 0
        length = 0
        i = 0
        
        if len(nums) < 1:
            return -1
            
        while i < len(nums):
            if nums[i] == val:
                i += 1
            else:
                break
                
            
        while index < len(nums):
            if nums[index] != val:
                nums[length] = nums[index]
                index += 1
                length += 1
            else:
                index += 1
        
        return length
