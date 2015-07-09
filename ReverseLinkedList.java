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
The time complexity is O(n) and the space complexity is O(1).

Something about Java gramma:
it is a 'null' pointer;
Pay attention to Java's declair: ListNode myNode; or ListNode myNode = new ListNode(45);
In if sentances, the condition should be in "()", and for the an instance of class, it should be 'if( null == head)',
instead of 'if(head)', since the second one is for pointers in C, here it is an instance.
'''

/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
public class Solution {
    public ListNode reverseList(ListNode head) {
        if(null == head)
            return null;
        if(null == head.next)
            return head;
        
        ListNode tail, current, tmp;
        tail = head;
        current = tail.next;
        tmp = current.next;
        
        while( null != current){
            current.next = head;
            tail.next = tmp;
            head = current;
            
            if(null != tmp){
                current = tmp;
                tmp = tmp.next;
            }
            else break;
        }
        
        return head;
    }
}
