# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution (object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        num1 = num2 = 0
        while (l1):
            num1 = num1 * 10 + l1.val
            l1 = l1.next
        while (l2):
            num2 = num2 * 10 + l2.val
            l2 = l2.next
        final = str (num1 + num2)

        temp = ListNode (int (final[0]))
        check = temp
        for i in range (1, len (final)):
            temp.next = ListNode (int (final[i]))
            temp = temp.next

        return check