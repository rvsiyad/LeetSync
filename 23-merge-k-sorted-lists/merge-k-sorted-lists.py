# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 0:
            return None
        
        if len(lists) == 1:
            return lists[0]
        # We can basically do a sorting algorithm like merge sort. Take each list and its neighbour, keep merging them.
        # Pop two from end of the list? Merge them and add back to list?

        while len(lists) > 1:
            mergedList = []

            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = lists[i + 1] if i + 1 < len(lists) else None

                mergedList.append(self.mergeTwoLists(l1, l2))

            lists = mergedList
        
        return lists[0]
    
    def mergeTwoLists(self, l1, l2):
        if not l1:
            return l2
        
        if not l2:
            return l1
        
        l1P, l2P = l1, l2

        dummyNode = ListNode()
        curr = dummyNode

        while l1P and l2P:
            if l1P.val < l2P.val:
                curr.next = l1P
                l1P = l1P.next
            else:
                curr.next = l2P
                l2P = l2P.next
            
            curr = curr.next
        
        if l1P:
            curr.next = l1P
        
        if l2P:
            curr.next = l2P
        
        return dummyNode.next
