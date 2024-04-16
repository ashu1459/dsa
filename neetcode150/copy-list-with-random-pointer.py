"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        oldToNew = {None: None}

        curr = head
        while curr:
            oldToNew[curr] = Node(curr.val)
            curr = curr.next
        
        curr = head
        while curr:
            copy = oldToNew[curr]
            copy.next = oldToNew[curr.next]
            copy.random = oldToNew[curr.random]
            curr = curr.next

        return oldToNew[head]


        # Solution-2: O(1) space
        # this can be done in O(1) space by interleaving the old and new nodes while creating.
        #  It is possible if you change input linked list with appending clonned values between existed nodes in linked list.