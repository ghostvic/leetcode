'''
leetcode: NO. 217	Contains Duplicate
Given an array of integers, find if the array contains any duplicates. 
Your function should return true if any value appears at least twice in the array, 
and it should return false if every element is distinct.
'''

'''
My solution is using a dict, and it is o(n) of time complexity 
'''
class Solution:
    # @param {integer[]} nums
    # @return {boolean}
    def containsDuplicate(self, nums):
        if len(nums) == 0:
            print "List is empty!"
            return False
        myDict = {}
        for i in nums:
            if myDict.has_key(i):
                return True
            else:
                myDict[i] = 0
        
        return False
