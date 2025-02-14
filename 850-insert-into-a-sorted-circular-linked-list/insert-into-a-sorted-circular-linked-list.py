"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next
"""

class Solution(object):
    def insert(self, head, insertVal):
        """
        :type head: Node
        :type insertVal: int
        :rtype: Node
        """

        if not head:
            newNode = Node(insertVal)

            newNode.next = newNode
            return newNode
        
        curr = head

        while curr and curr.next != head:
            if curr.val <= insertVal < curr.next.val:
                newNode = Node(insertVal, curr.next)
                curr.next = newNode
                
                return head

            elif curr.val > curr.next.val:
                if insertVal >= curr.val or insertVal < curr.next.val:
                    newNode = Node(insertVal, curr.next)
                    curr.next = newNode

                    return head

            curr = curr.next
        
        newNode = Node(insertVal, curr.next)

        curr.next = newNode

        return head