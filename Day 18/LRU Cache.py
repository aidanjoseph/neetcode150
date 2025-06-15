class Node:
   def __init__(self, key, val):
       self.key, self.val = key, val
       self.prev = self.next = None
class LRUCache:


   def __init__(self, capacity: int):
       self.capacity = capacity
       self.storage = {}
       self.left, self.right = Node(0,0), Node(0,0)
       #left = LRU, #right = MRU
       self.left.next, self.right.prev = self.right, self.left       


   def get(self, key: int) -> int:
       if key in self.storage:
           self.remove(self.storage[key])
           self.insert(self.storage[key])
           return self.storage[key].val
       return -1


   def remove(self, node):
       prev, nxt = node.prev, node.next
       prev.next, nxt.prev = nxt, prev


   def insert(self, node):
       prev, nxt = self.right.prev, self.right
       prev.next = nxt.prev = node
       node.next, node.prev = nxt, prev
      


   def put(self, key: int, value: int) -> None:
       if key in self.storage:
           self.remove(self.storage[key])
       self.storage[key] = Node(key, value)
       self.insert(self.storage[key])
       if len(self.storage) > self.capacity:
           #delete LRU
           lru = self.left.next
           self.remove(lru)
           del self.storage[lru.key]




      




# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
