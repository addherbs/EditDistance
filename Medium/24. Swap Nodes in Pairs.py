# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        temp = head
        count = 1
        
        prev = head
        curr = head
        
        while (temp != None):
            temp = temp.next
            if (count == 2):
                count = 1
                dummy = prev.val
                prev.val = curr.val
                curr.val = dummy
                prev = curr
                curr = curr.next
                continue
            
            prev = curr
            curr = curr.next
            count += 1

        
    
        return head