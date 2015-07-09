'''
Reverse a singly linked list.
'''

'''
Solution: there should be 4 pointers: 
a. head: the first node at any time
b. current: the current node which is processed
c. tmp: the next node which will be processed
d. tail: the last node of the list, it should point to the first node at the beginning and not be changed.

So basic process is: 
current.next = head
tail.next = tmp
head = current 
current = tmp
tmp = tmp.next
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param {ListNode} head
    # @return {ListNode}
    def reverseList(self, head):
        if None == head:
            return None
        if None == head.next:
            return head
        
        tail = head
        current = head.next
        tmp = current.next
        
        while None != current:
            current.next = head
            tail.next = tmp
            head = current
            
            if None != tmp:
                current = tmp
                tmp = tmp.next
            else:
                break
        
        return head
            
        
