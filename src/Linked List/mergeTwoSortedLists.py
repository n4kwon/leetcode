class Solution:
    # Iterative Approach
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        prehead = ListNode(-1)
        prev = prehead
        while list1 and list2:
            if list1.val <= list2.val:
                prev.next = list1
                list1 = list1.next
            else:
                prev.next = list2
                list2 = list2.next
        if list1:
            prev.next = list1
        elif list2:
            prev.next = list2
        return prehead.next
    
    # Recursive Approach
    def mergeTwoListsRecursively(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None:
            return list2
        elif list2 is None:
            return list1
        elif list1.val < list2.val:
            list1.next = self.mergeTwoListsRecursively(list1.next, list2)
            return list1
        else:
            list2.next = self.mergeTwoListsRecursively(list1, list2.next)
            return list2
