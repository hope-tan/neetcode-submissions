# given 2 non-empty linked lists (l1, l2) representing non-negative int where each node is 1 digit
# stored in reverse place value
# no leading 0 except 0 itself
# return sum

# input: 2 linked lists
# output: 1 linked list that is the sum

# clarifications
    # will l1 and l2 be the same size? no
    # carry to the next place value if sum > 10
    # output should also be in reverse order

# class ListNode:
#     def __init__(self, val, nxt):
#         self.val = val
#         self.nxt = nxt

class Solution:
    def addTwoNumbers(self, l1 : Optional[ListNode], l2 : Optional[ListNode]) -> Optional[ListNode]:
        l3 = ListNode()
        curr1 = l1
        curr2 = l2
        curr3 = l3
        carry = 0

        while curr1 or curr2 or carry:
            v1 = curr1.val if curr1 else 0
            v2 = curr2.val if curr2 else 0
            if carry + v1 + v2 >= 10:
                curr3.val = carry + v1 + v2 - 10
                carry = 1
            else:
                curr3.val = carry + v1 + v2
                carry = 0

            curr1 = curr1.next if curr1 else 0
            curr2 = curr2.next if curr2 else 0
            if curr1 or curr2 or carry:
                curr3.next = ListNode()
                curr3 = curr3.next
        return l3 

    # make a ptr for each l1 and l2
    # make bool to track if carrying is needed (1 means carry)
    # if the sum of ptr values and carry >= 10, toggle carry bool to 1
    # if not, just update sum in l3
    # move l1 and l2 and l3 to next
    # return the result list

