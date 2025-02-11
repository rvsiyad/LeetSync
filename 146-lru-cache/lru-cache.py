class ListNode:
    def __init__(self, key = 0, val=0, prev=None, next=None):
        self.key = key
        self.val = val
        self.prev = prev
        self.next = next

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        # Each key will point to a node in hashmap
        self.hashmap = {}
        self.length = 0

        self.tail = ListNode()
        self.head = ListNode()

        self.tail.next = self.head
        self.head.prev = self.tail

    def add(self, node):
        prev = self.head.prev

        prev.next = node
        node.prev = prev
        node.next = self.head
        self.head.prev = node

    def remove(self, node):
        prev, next = node.prev, node.next

        prev.next = next
        next.prev = prev
        node.prev, node.next = None, None

    def get(self, key: int) -> int:
        # We want to get that nodes val and return it.
        # The hashmap stores a key which points to the node
        # We want to hold the value of the node
        # Remove node from current position and add to end.
        if key in self.hashmap:
            node = self.hashmap[key]

            self.remove(node)
            self.add(node)

            return node.val
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        # Update val of key if exists
        if key in self.hashmap:
            node = self.hashmap[key]
            node.val = value

            self.remove(node)
            self.add(node)
        else:
            if self.length >= self.capacity:
                nodeToRemove = self.tail.next
                del self.hashmap[nodeToRemove.key]

                self.remove(nodeToRemove)
                self.length -= 1

            node = ListNode(key, value)
            self.hashmap[key] = node

            self.add(node)
            self.length += 1
        
        
        
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)