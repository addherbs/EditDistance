import java.util.*; 
/**
445. Add Two Numbers II
Medium

995

128

Add to List

Share
You are given two non-empty linked lists representing two non-negative integers. The most significant digit comes first and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Follow up:
What if you cannot modify the input lists? In other words, reversing the lists is not allowed.

Example:

Input: (7 -> 2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 8 -> 0 -> 7

 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */

class Solution {
   public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
      int len1 = length(l1);
      int len2 = length(l2);
      
      Stack<Integer> stk1 = new Stack<Integer>();
      Stack<Integer> stk2 = new Stack<Integer>();

      if (len1 < len2) padZeros(stk1, len2 - len1);
      if (len2 < len1) padZeros(stk2, len1 - len2);

      addElementsToStackFromList(stk1, l1);
      addElementsToStackFromList(stk2, l2);

      return generateAnsFromStacks(stk1, stk2);

   }

   private static ListNode generateAnsFromStacks(Stack<Integer> stk1, Stack<Integer> stk2) {
      ListNode ansNode = null;
      ListNode temp = null;
      
      int carry = 0, sum = 0;
       
      while (!stk1.empty() || carry != 0) {
         sum = carry;
         if (!stk1.empty()){
            sum += (int) stk1.pop() + (int) stk2.pop();
         }
         carry = sum / 10;
         
         temp = new ListNode(sum % 10);
         temp.next = ansNode;
         ansNode = temp;
         
      }
      return ansNode;
   }


   private static void addElementsToStackFromList(Stack<Integer> stk, ListNode l) {
      while (l != null) {
         stk.push(l.val);
         l = l.next;
      }
   }

   private static void padZeros(Stack<Integer> stk, int count) {
      for (int i= 0; i < count; i++){
         stk.push(0);
      }
   }

   private static int length(ListNode l) {
      int count = 0;
      while (l != null) {
         count++;
         l = l.next;
      }
      return count;
   }
}
