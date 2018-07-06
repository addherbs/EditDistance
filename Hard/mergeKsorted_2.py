# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeKLists(self, lists):
        if (not lists):
            return None
        elif (len (lists) == 1):
            return lists[0]
        elif (len (lists) < 3):
            return self.merge (lists[0], lists[1])
        else:
            temp = self.merge (lists[0], lists[1])
            i = 2
            while (i < len (lists)):
                temp = self.merge (temp, lists[i])
                i += 1
                # self.print_l(temp)
            return temp

    def merge(self, l1, l2):
        point = head   = ListNode (0)

        while l1 and l2:
            if l1.val <= l2.val:
                point.next = l1
                l1 = l1.next
            else:
                point.next = l2
                l2 = l1
                l1 = point.next.next
            point = point.next
        if not l1:
            point.next = l2
        else:
            point.next = l1
        return head.next