class Node:

    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}
        # dummy nodes to avoid None cases in prev and next
        self.head = Node(0, 0) # LRU
        self.tail = Node(0, 0) # MRU

        self.head.next, self.tail.prev = self.tail, self.head
    
    # remove from cache and LL
    def remove(self, node):
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = nxt, prev

    # insert at the end of LL
    def insert(self, node):
        prev, nxt = self.tail.prev, self.tail
        prev.next = nxt.prev = node
        node.prev, node.next = prev, nxt

    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache[key].val = value
            self.remove(self.cache[key])
        else:
            self.cache[key] = Node(key, value)
        
        self.insert(self.cache[key])

        if len(self.cache) > self.cap:
            lru = self.head.next
            self.remove(lru)
            del self.cache[lru.key]
        

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)