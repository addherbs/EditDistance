# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if (head is None):
            return True

        value = []
        node = ListNode (head.val)

        node.next = head.next

        while (node != None):
            value.append (node.val)
            node = node.next

        return True if (value == value[::-1]) else False
