# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if k == 0 or head is None or head.next is None:
            return head

        dummy = ListNode()
        prev = None
        lastCheckpoint = dummy

        while head:
            count = 0
            start = head
            valid = True

            temp = start
            tempCount = 0

            while tempCount < k and temp:
                temp = temp.next
                tempCount += 1

            if tempCount != k:
                break

            while valid and head and count < k:
                temp = head.next
                head.next = prev
                prev = head
                head = temp
                count += 1

            lastCheckpoint.next = prev
            lastCheckpoint = start
            start.next = head

        return dummy.next