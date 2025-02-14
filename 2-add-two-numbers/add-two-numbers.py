# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        num = ""
        carry = 0

        dummyNode = ListNode()
        curr = dummyNode

        while l1 or l2 or carry:
            l1Val = l1.val if l1 else 0
            l2Val = l2.val if l2 else 0

            curSum = l1Val + l2Val + carry

            carry = curSum // 10
            curr.next = ListNode(curSum % 10)

            curr = curr.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        
        return dummyNode.next



        