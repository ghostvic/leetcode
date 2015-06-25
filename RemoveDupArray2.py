'''
Given a sorted array, remove the duplicates in place such that each element appear at most twice and return the new length.
Do not allocate extra space for another array, you must do this in place with constant memory.
For example,
Given input array A = [1,1,1,2],
Your function should return length = 3, and A is now [1,1,2].
'''

'''
For this problem, the most important thing is we only skip the element if it appears more than twice. So using the first
algrithm of removing duplicate array, we use a var length to indicate the length we want, and move the eligible element 
(the appearance is less than 3, so we also need another various to count the appearance) to the position(nums[length]).
'''
class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def removeDuplicates(self, nums):
        if len(nums) < 3:
            return len(nums)
        
        length = 1
        i = 1
        count = 1
        tmp = nums[0]

        while i < len(nums):
            if tmp != nums[i]:
                tmp = nums[i]
                nums[length] = nums[i]
                count = 1
                length += 1
            else:
                count += 1
                if count < 3:
                    nums[length] = nums[i]
                    length += 1
            
            i += 1
        
        return length
