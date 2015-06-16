'''
My Submissions Question Solution 
Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times.

You may assume that the array is non-empty and the majority element always exist in the array.
'''

#Solution: We have to go through every element in the list, and build a dict with keys are the elements and values are the number of 
#number of its appearence. So that the time complexity is O(n)

class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def majorityElement(self, nums):
        if len(nums) < 1:
            return None
            
        myDict = {}
        mar = len(nums)/2

        for i in nums:
            if myDict.has_key(i):
                myDict[i] += 1
            else:
                myDict[i] = 1
                
            if myDict[i] > mar:
                return i
