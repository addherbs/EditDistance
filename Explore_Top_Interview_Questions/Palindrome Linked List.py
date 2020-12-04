"""
Palindrome Linked List

Solution
Given a singly linked list, determine if it is a palindrome.

Example 1:

Input: 1->2
Output: false
Example 2:

Input: 1->2->2->1
Output: true
Follow up:
Could you do it in O(n) time and O(1) space?
"""



# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if not head: return True
        
        mid = head
        forward = head.next
        while forward and forward.next:
            mid = mid.next
            forward = forward.next.next
        
        rev_node = self.rev(mid.next)
        mid.next = rev_node
        
        start = head
        temp = mid.next
        while temp != None:
            if start.val != temp.val: return False
            start = start.next
            temp = temp.next
        
        mid.next = self.rev(mid.next)
        return True
    
    
    def rev(self, node):
        prev = None
        curr = node
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        
        return prev