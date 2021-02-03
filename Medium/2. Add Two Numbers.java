/**

2. Add Two Numbers
Medium

6671

1732

Add to List

Share
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example:

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.

 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
class Solution {
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        
        ListNode ansList = new ListNode(0);
        ListNode tempAns = ansList;
        
        ListNode t1 = l1, t2 = l2;
        
        int carry = 0;
        int sum = carry;
        
        while (t1 != null || t2 != null || carry != 0) {
            System.out.println(carry);
                
            sum = carry;
            if (t1 != null) {
                sum += t1.val;
                t1 = t1.next;
            }
            if (t2 != null) {
                sum += t2.val;
                t2 = t2.next;
            }
            
            tempAns.next = new ListNode(sum % 10);
            tempAns = tempAns.next;
            
            carry = sum / 10;
            
        }
        return ansList.next;
    }
}