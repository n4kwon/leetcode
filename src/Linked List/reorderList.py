class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return
        slow = head
        fast = head
        # 2 pointer algorithm to find middle of linked list
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        # cut of linked list at midpoint to form two separate
        curr = slow.next
        slow.next = None

        prev = None
        while curr:
            temp = curr.next
            curr.next = prev

            prev = curr
            curr = temp
        # prev is head of reversed

        # build up linkedlist using given pattern
        while prev:
            temp1 = head.next
            temp2 = prev.next

            head.next = prev
            prev.next = temp1

            head = temp1
            prev = temp2