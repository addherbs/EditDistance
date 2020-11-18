"""
Copy List with Random Pointer
Medium

4141

746

Add to List

Share
A linked list is given such that each node contains an additional random pointer which could point to any node in the list or null.

Return a deep copy of the list.

The Linked List is represented in the input/output as a list of n nodes. Each node is represented as a pair of [val, random_index] where:

val: an integer representing Node.val
random_index: the index of the node (range from 0 to n-1) where random pointer points to, or null if it does not point to any node.
 

Example 1:


Input: head = [[7,null],[13,0],[11,4],[10,2],[1,0]]
Output: [[7,null],[13,0],[11,4],[10,2],[1,0]]
Example 2:


Input: head = [[1,1],[2,1]]
Output: [[1,1],[2,1]]
Example 3:



Input: head = [[3,null],[3,0],[3,null]]
Output: [[3,null],[3,0],[3,null]]
Example 4:

Input: head = []
Output: []
Explanation: Given linked list is empty (null pointer), so return null.
 

Constraints:

-10000 <= Node.val <= 10000
Node.random is null or pointing to a node in the linked list.
The number of nodes will not exceed 1000.
"""

"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

# O(N) space solution
class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        vis = {}
        
        if not head:
            return None
        
        vis[head] = Node(head.val)
        root = vis[head]
        
        root.next = self.recurse(head.next, vis)
        root.random = self.recurse(head.random, vis)
        
        return root
    
    def recurse(self, original, vis):

        if original in vis:
            return vis[original]
        
        if not original: return None
        
        temp = Node(original.val)
        vis[original] = temp
        temp.next = self.recurse(original.next, vis)
        temp.random = self.recurse(original.random, vis)
        
        return temp
    
    

# O(1) space solution

"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':

        if not head: return None

        pointer = head

        while pointer:

            new_node = Node(pointer.val)
            new_node.next = pointer.next
            pointer.next = new_node

            pointer = new_node.next

        pointer = head

        while pointer:
            pointer.next.random = pointer.random.next if pointer.random else None
            pointer = pointer.next.next

        old_list = head
        new_list = head.next
        ans = new_list

        while old_list:
            old_list.next = old_list.next.next
            new_list.next = new_list.next.next if new_list.next else None
            old_list = old_list.next
            new_list = new_list.next

        return ans