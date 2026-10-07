# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Optional because the ListNode could be null
        # given beginning/head, reverse and return new head
        # for each node:
            # save curr.next
            # make curr.next = prev (reversing link)
            # advance prev to curr
            # advance curr to curr.next
        # do this until curr is NULL
        curr = head
        prev = None
        
        while curr:
            saved = curr.next
            curr.next = prev
            prev = curr
            curr = saved
        return prev