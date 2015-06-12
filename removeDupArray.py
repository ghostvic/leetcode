'''
Given a sorted array, remove the duplicates in place such that each element appear only once and return the new length.

Do not allocate extra space for another array, you must do this in place with constant memory.

For example,
Given input array A = [1,1,2],

Your function should return length = 2, and A is now [1,2].
'''

'''
The key point for this AC algrithm is that we have to move the element with differnt value to the right place : nums[length].
So introducing the var length is key.
'''

class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def removeDuplicates(self, nums):
        if len(nums) == 0:
            return -1
        elif len(nums) == 1:
            return 1
        
        index = 1
        length = 1
        tmp = nums[0]
            
        while index < len(nums):
            if tmp != nums[index]:
                tmp = nums[index]
                nums[length] = nums[index]
                length += 1
            index += 1
        
        return length

#The function below is not accepted by the system beacuse I used list.pop(), but I leave it here.

class Solution:
    # @param a list of integers
    # @return an integer
    def removeDuplicates(self, A):
        if len(A) == 1:
            return len(A)
        elif len(A) <= 0:
            return -1
        else:
            remain = len(A)
            i = 1
            while remain > 0:
                if A[i] == A[i-1]:
                    A.pop(i)
                    if len(A) > 1:
                        remain = len(A) - i
                    else:
                        return len(A)
                else:
                    i += 1
                    remain = len(A) - i

            return len(A)
