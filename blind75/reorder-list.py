# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # find middle using slow(+1) and fast(+2) pointer
        # reverse second half
        # merge the first and second half

        slow, fast = head, head

        # loop ends when fast pointer is at end of list
        # and we get middle Node(slow pointer)
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        # reverse second half
        second = slow.next
        prev = slow.next = None

        while second:
            temp = second.next
            second.next = prev
            prev = second
            second = temp
        
        # merge first and second/reversed list
        first, second = head, prev
        while second:
            temp, temp2 = first.next, second.next
            second.next, first.next = temp, second

            first, second = temp, temp2
