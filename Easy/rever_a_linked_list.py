# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if (head is None):
            return head

        temp = []
        while (head):
            temp.append (head.val)
            head = head.next
        temp = temp[::-1]

        newHead = ListNode (0)
        head = newHead
        for each in temp:
            head.next = ListNode (each)
            head = head.next

        return newHead.next

#inplace sorting

class Solution:
    def reverseList(self, head):

        curr = head
        nxt = None
        prev = None

        while ( curr != None ):
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        return prev