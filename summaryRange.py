'''
Given a sorted integer array without duplicates, return the summary of its ranges.
For example, given [0,1,2,4,5,7], return ["0->2","4->5","7"].
'''

'''
This problem doesn't need too many variables. The time complexity is O(n)
'''
class Solution:
    # @param {integer[]} nums
    # @return {string[]}
    def summaryRanges(self, nums):
        if len(nums) < 1:
            return []
        result = []
        if len(nums) == 1:
            result.append("%d" % nums[0])
            return result
        
        i = 0
        while i < len(nums):
            tmp = nums[i]
            while (i+1 < len(nums)) and (nums[i+1] - nums[i] == 1):
                i += 1
            if tmp != nums[i]:
                result.append("%d->%d" % (tmp,nums[i]))
            else:
                result.append("%d" % tmp)
            i += 1
       
        return result
