/**
19. Remove Nth Node From End of List
Medium

2427

180

Add to List

Share
Given a linked list, remove the n-th node from the end of list and return its head.

Example:

Given linked list: 1->2->3->4->5, and n = 2.

After removing the second node from the end, the linked list becomes 1->2->3->5.
Note:

Given n will always be valid.

Follow up:

Could you do this in one pass?

 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
class Solution {
    public ListNode removeNthFromEnd(ListNode head, int n) {
        
        ListNode p = head, q = head;
        int count = 0;
        
        while (p != null) {
            if (count == n) break;
            count++;
            p = p.next;
        }
        if (p == null && n == count) {
            head = head.next;
        }
        while (p != null) {
            if (p.next == null) {
                q.next = q.next.next;
            }
            p = p.next;
            q = q.next;
        }
        return head;
    }
}