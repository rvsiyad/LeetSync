class ListNode:
    def __init__(self, val, prev, nxt):
        self.val = val
        self.prev = prev
        self.nxt = nxt

class MyCircularDeque:
    def __init__(self, k: int):
        self.maxSize = k
        self.currentSize = 0
        self.head = ListNode(0, None, None)
        self.tail = ListNode(0, None, None)
        self.head.nxt = self.tail
        self.tail.prev = self.head

    def insertFront(self, value: int) -> bool:
        if self.currentSize < self.maxSize:
            newNode = ListNode(value, None, None)
            prev, nxt = self.head, self.head.nxt
            newNode.nxt = nxt
            newNode.prev = prev
            prev.nxt = newNode
            nxt.prev = newNode

            self.currentSize += 1
            return True
        else:
            return False
        

    def insertLast(self, value: int) -> bool:
        if self.currentSize < self.maxSize:
            newNode = ListNode(value, None, None)
            prev, nxt = self.tail.prev, self.tail
            newNode.nxt = nxt
            newNode.prev = prev
            prev.nxt = newNode
            nxt.prev = newNode

            self.currentSize += 1
            return True
        else:
            return False

    def deleteFront(self) -> bool:
        if self.currentSize < 1:
            return False
        else:
            self.head.nxt = self.head.nxt.nxt
            self.head.nxt.prev = self.head
            self.currentSize -= 1
            return True

    def deleteLast(self) -> bool:
        if self.currentSize < 1:
            return False
        else:
            self.tail.prev = self.tail.prev.prev
            self.tail.prev.nxt = self.tail
            self.currentSize -= 1
            return True

    def getFront(self) -> int:
        if self.currentSize < 1:
            return -1
        else:
            return self.head.nxt.val

    def getRear(self) -> int:
        if self.currentSize < 1:
            return -1
        else:
            return self.tail.prev.val

    def isEmpty(self) -> bool:
        if self.currentSize == 0:
            return True
        else:
            return False

    def isFull(self) -> bool:
        if self.currentSize == self.maxSize:
            return True
        else:
            return False
        


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()