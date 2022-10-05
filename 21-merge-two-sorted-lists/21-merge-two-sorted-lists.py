# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2
        if not list2:
            return list1
        
        dummy = ListNode()
        curr = dummy
        
        while list1 and list2:
            # sort starting from smallest
            if list1.val < list2.val:
                curr.next = list1
                list1 = list1.next
            # if list2 has smallaer value
            else:
                curr.next = list2
                list2 = list2.next
            # current node points to the next node
            curr = curr.next
        # after the loop iteration, only the tail element would be left, so discard(ignore) it
        curr.next = list1 if list1 else list2
        # return dummy's next pointer, which is current node(head)
        return dummy.next
                