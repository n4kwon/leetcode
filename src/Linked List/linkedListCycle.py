class Solution:
    # HashSet Solution
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        seen = set()
        while head:
            if head in seen:
                return True
            else:
                seen.add(head)
            head = head.next
        return False
    
    # 2 Pointer Floyd's Algorithm
    def FloydHasCycle(self, head: Optional[ListNode]) -> bool:
        if head is None:
            return False
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False