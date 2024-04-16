# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # head = None
        # hashmap = {}
        # stack_left = [float("-infinity")]
        # stack_right = [float("infinity")]

        # for l in lists:
        #     curr = l
        #     while curr:
        #         nxt = curr.next

        #         if curr.val in hashmap:
        #             temp = hashmap[curr.val].next
        #             hashmap[curr.val].next = ListNode(curr.val, temp)
        #             curr = hashmap[curr.val].next
        #         else:
        #             while curr.val < stack_left[-1]:
        #                 stack_right.append(stack_left.pop())
        #             while curr.val > stack_right[-1]:
        #                 stack_left.append(stack_right.pop())
                    
        #             if stack_left[-1] > float("-infinity"):
        #                 temp = hashmap[stack_left[-1]].next
        #                 hashmap[stack_left[-1]].next = ListNode(curr.val, temp)
        #                 curr = hashmap[stack_left[-1]].next
        #             else:
        #                 head = ListNode(curr.val, head)
        #                 curr = head

        #             stack_left.append(curr.val)

        #         hashmap[curr.val] = curr

        #         curr = nxt
            
        # return head

        # Soluion-2
        # take two lists and merge them, keeping doing this untill there's one list left
        if len(lists) < 1:
            return None

        while len(lists) > 1:
            merged = []
            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = lists[i+1] if (i + 1) < len(lists) else None
                merged.append(self.mergeList(l1, l2))
            lists = merged
        
        return lists[0]

    def mergeList(self, l1, l2):
        dummy = ListNode()
        tail = dummy
        
        while l1 and l2:
            if l1.val < l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next

        if l1:
            tail.next = l1
        if l2:
            tail.next = l2
        
        return dummy.next

