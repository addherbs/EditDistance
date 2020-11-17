"""
Merge k Sorted Lists

Solution
You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

Merge all the linked-lists into one sorted linked-list and return it.

 

Example 1:

Input: lists = [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]
Explanation: The linked-lists are:
[
  1->4->5,
  1->3->4,
  2->6
]
merging them into one sorted list:
1->1->2->3->4->4->5->6
Example 2:

Input: lists = []
Output: []
Example 3:

Input: lists = [[]]
Output: []
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        from heapq import heappush, heappop
        heap = []
        for i, each in enumerate(lists):
            if each:
                heappush(heap, [int(each.val), i, each.next])
        
        ans = ListNode(0)
        it = ans
        while heap:
            val, i, nxt = heappop(heap)
            it.next = ListNode(val)
            it = it.next
            
            if nxt:
                heappush(heap, [int(nxt.val), i, nxt.next])
        
        return ans.next