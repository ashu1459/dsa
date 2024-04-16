# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        carry = 0
        head = ListNode()
        new_list = head

        while l1 or l2:
            l1_val = l1.val if l1 else 0
            l2_val = l2.val if l2 else 0

            total = l1_val + l2_val + carry
            carry = total // 10
            val = total % 10
            new_list.next = ListNode(val)
            
            new_list = new_list.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        
        if carry > 0:
            new_list.next = ListNode(carry)

        return head.next


