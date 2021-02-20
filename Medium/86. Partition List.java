/**
	86. Partition List
Medium

922

245

Add to List

Share
Given a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.

You should preserve the original relative order of the nodes in each of the two partitions.

Example:

Input: head = 1->4->3->2->5->2, x = 3
Output: 1->2->2->4->3->5

 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
class Solution {
    public ListNode partition(ListNode head, int x) {
        
      
      if (head == null) return null;

      ListNode l1Start = null, l1End = null, l2Start = null, l2End = null;

      while (head != null) {
         if (head.val < x) {
            if (l1Start == null) {
               l1Start = new ListNode(head.val);
               l1End = l1Start;
            } else {
               l1End.next = new ListNode(head.val);
               l1End = l1End.next;
            }
         } else {
            if (l2Start == null) {
               l2Start = new ListNode(head.val);
               l2End = l2Start;
            } else {
               l2End.next = new ListNode(head.val);
               l2End = l2End.next;
            }
         }
         head = head.next;
      }
      if (l1Start != null) {
          l1End.next = l2Start;
          return l1Start;
      }
      return l2Start;
   }
}