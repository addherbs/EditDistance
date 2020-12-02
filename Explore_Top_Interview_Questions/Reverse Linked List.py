"""
Reverse Linked List

Solution
Reverse a singly linked list.

Example:

Input: 1->2->3->4->5->NULL
Output: 5->4->3->2->1->NULL
Follow up:

A linked list can be reversed either iteratively or recursively. Could you implement both?
"""

# Using Recursion

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        
        head, nodes =  self._recurse(head)
        return head
        
    def _recurse(self, node):
        if not node or not node.next:
            return node, node
        
        head, future_nodes = self._recurse(node.next)
        node.next = None
        future_nodes.next = node
        
        return head, node