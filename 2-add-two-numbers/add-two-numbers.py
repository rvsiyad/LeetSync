# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l1String, l2String = "", ""

        l1Pointer, l2Pointer = l1, l2

        while l1Pointer:
            l1String += str(l1Pointer.val)
            l1Pointer = l1Pointer.next
        
        while l2Pointer:
            l2String += str(l2Pointer.val)
            l2Pointer = l2Pointer.next
    
        l1String = l1String[::-1]
        l2String = l2String[::-1]


        newTotal = int(l1String) + int(l2String)
        newTotal = str(newTotal)

        dummyNode = ListNode()
        curr = dummyNode

        for i in range(len(newTotal)-1,-1,-1):
            curr.next = ListNode(int(newTotal[i]))
            curr = curr.next
        
        return dummyNode.next