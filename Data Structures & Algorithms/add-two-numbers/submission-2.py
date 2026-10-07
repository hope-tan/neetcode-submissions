# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # add the corresponding nodes of the lists and if their sum exceeds 10, add 1 to the next place value
        l3 = ListNode() # result list

        curr1 = l1
        curr2 = l2
        curr3 = l3
        carry = 0

        while curr1 or curr2 or carry:
            v1 = curr1.val if curr1 else 0
            v2 = curr2.val if curr2 else 0
            if v1 + v2 + carry >= 10:
                curr3.val = v1 + v2 - 10 + carry
                carry = 1
            else:
                curr3.val = v1+ v2 + carry
                carry = 0
            curr1 = curr1.next if curr1 else 0
            curr2 = curr2.next if curr2 else 0
            if curr1 or curr2 or carry:
                curr3.next = ListNode()
                curr3 = curr3.next
        return l3
        