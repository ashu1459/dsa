# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Solution-1: using backtracking
        # backtrack method to get n from end of LL 
        # def backtrack(node, n, prev):
        #     if node.next:
        #         count, remaining = backtrack(node.next, n, node)
        #         node.next = remaining
        #     else:
        #         count = 1

        #     return count + 1, node.next if count == n else node

        # count, head = backtrack(head, n, None)

        # return head

        # Solution-2: using two points
        # take a dummy node to shift pointer one left for previous elem
        dummy = ListNode(0, head)

        left, right = dummy, head

        while right:
            # maintain the distance between right and left by "n"
            if n > 0:
                n -= 1
            else:
                left = left.next
            
            right = right.next

        # We got the node previous to the one we need to remove
        left.next = left.next.next

        return dummy.next


