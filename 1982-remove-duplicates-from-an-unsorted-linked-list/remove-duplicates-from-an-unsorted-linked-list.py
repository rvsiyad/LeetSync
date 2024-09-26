# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicatesUnsorted(self, head: ListNode) -> ListNode:
        curr = head
        valCount = {}

        while curr:
            valCount[curr.val] = 1 + valCount.get(curr.val, 0)
            curr = curr.next

        dummyNode = ListNode()
        dummyCurr = dummyNode
        curr = head

        while curr:
            if valCount[curr.val] == 1:
                dummyCurr.next = ListNode(curr.val)
                dummyCurr = dummyCurr.next
            
            curr = curr.next
        
        return dummyNode.next

