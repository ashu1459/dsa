# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if head is None:
            return head

        # Solution:Linear - TC: O(n)
        # prev = None

        # while head:
        #     temp = head.next
        #     head.next = prev

        #     prev = head
        #     head = temp

        # return prev

        # Solution-2: recursive
        if head.next is None:
            return head
        else:
            reversed_ll = self.reverseList(head.next)
            head.next.next = head
            head.next = None
        
        return reversed_ll
    
        # Solution-3: recursive
        # return self.recursiveList(head, None)
    
    # def recursiveList(self, curr, prev):
    #     if curr is None:
    #         return prev

    #     temp = curr.next
    #     curr.next = prev

    #     return self.recursiveList(temp, curr)


        

        