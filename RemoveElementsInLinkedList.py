'''
Leetcode NO.203	Remove Linked List Elements
Remove all elements from a linked list of integers that have value val.

Example
Given: 1 --> 2 --> 6 --> 3 --> 4 --> 5 --> 6, val = 6
Return: 1 --> 2 --> 3 --> 4 --> 5
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param {ListNode} head
    # @param {integer} val
    # @return {ListNode}
    def removeElements(self, head, val):
        #Empty list
        if not head:
            return head
        
        #One node list    
        if not head.next:
            if head.val == val:
                head = head.next
            return head
            
        newHead = head
        pre = head
        
        #Delete nodes in the beginning if they have the same val
        #After this loop, newHead, pre, head should point to the first non-val node.
        while head:
            if head.val == val:
                head = head.next
                pre = head
                newHead = head
            else:
                break
                
        while head:
            if head.val != val:
                pre = head
                head = head.next
            else:
                head = head.next
                pre.next = head
        return newHead
                
