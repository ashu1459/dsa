# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        # Solution-1
        # if not list1:
        #     return list2
        # elif not list2:
        #     return list1

        # if list1.val > list2.val:
        #     return self.mergeTwoLists(list2, list1)
        
        # res = list1

        # while list1 and list2:
        #     if list1.val == list2.val \
        #         or (list1.next and list1.next.val >= list2.val) \
        #         or list1.next is None:
        #         temp = list1.next
        #         temp2 = list2.next

        #         list1.next = list2
        #         list2.next = temp

        #         list2 = temp2

        #     list1 = list1.next

        # return res

        # Solution-2
        dummy = ListNode()
        tail = dummy

        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next

        if list1:
            tail.next = list1
        elif list2:
            tail.next = list2

        return dummy.next
