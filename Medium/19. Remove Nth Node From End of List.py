# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        
        temp = head
        total_nodes = 0
        while (temp != None):
            total_nodes += 1
            temp = temp.next
        
        prev = head
        curr = head
        
        if (n == total_nodes): return head.next
        
        if (n == 1):
            temp = head
            for i in range (total_nodes - 2):
                temp = temp.next
            temp.next = None
            return head
        
        for i in range (total_nodes - n):
            prev = curr
            curr = curr.next
        
        prev.next = curr.next
        
        return head