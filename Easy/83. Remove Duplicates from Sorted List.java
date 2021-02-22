import java.util.HashSet;

/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
 
class Solution {
    public ListNode deleteDuplicates(ListNode head) {
      HashSet<Integer> set = new HashSet<>();
      ListNode p = head, q = head;

      while(p != null) {
         if (set.contains(p.val)) {
            q.next = p.next;
            p = p.next;
         } else {
            set.add(p.val);
            q = p;
            p = p.next;
         }
      }
      return head;
    }
}
