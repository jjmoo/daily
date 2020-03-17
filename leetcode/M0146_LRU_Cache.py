class DequeNode:
    def __init__(self, k, x):
        self.key = k
        self.val = x
        self.past = None
        self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.cap = capacity
        self.cnt = 0
        self.head = None
        self.tail = None
        self.pool = {}

    def get(self, key: int) -> int:
        if key not in self.pool: return -1
        node = self.pool[key]
        self.__update(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.pool:
            node = self.pool[key]
            node.val = value
            self.__update(node)
            return
        if self.cnt == self.cap: self.pool.pop(self.__pop().key)
        else: self.cnt += 1
        self.pool[key] = DequeNode(key, value)
        self.__insert(self.pool[key])

    def __insert(self, node: DequeNode):
        if self.head:
            node.next = self.head
            self.head.past = node
        self.head = node
        if not self.tail: self.tail = node

    def __update(self, node: DequeNode):
        if node is self.head: return
        node.past.next = node.next
        if node is self.tail: self.tail = node.past
        else: node.next.past = node.past
        node.past = None
        self.__insert(node)

    def __pop(self):
        node = self.tail
        if node is self.head: self.head, self.tail = None, None
        else: self.tail, node.past.next = node.past, None
        return node


# cache = LRUCache(2)
# cache.put(1, 1)
# cache.put(2, 2)
# print(1, cache.get(1))
# cache.put(3, 3)
# print(-1, cache.get(2))
# cache.put(4, 4)
# print(-1, cache.get(1))
# print(3, cache.get(3))
# print(4, cache.get(4))

cache = LRUCache(2)
cache.put(2, 1)
cache.put(2, 2)
print(cache.get(2))
cache.put(1, 1)
cache.put(4, 1)
print(cache.get(2))


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)


# Design and implement a data structure for Least Recently Used (LRU) cache. It should support the following operations: get and put.

# get(key) - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
# put(key, value) - Set or insert the value if the key is not already present. When the cache reached its capacity, it should invalidate the least recently used item before inserting a new item.

# The cache is initialized with a positive capacity.

# Follow up:
# Could you do both operations in O(1) time complexity?

# Example:

# LRUCache cache = new LRUCache( 2 /* capacity */ );

# cache.put(1, 1);
# cache.put(2, 2);
# cache.get(1);       // returns 1
# cache.put(3, 3);    // evicts key 2
# cache.get(2);       // returns -1 (not found)
# cache.put(4, 4);    // evicts key 1
# cache.get(1);       // returns -1 (not found)
# cache.get(3);       // returns 3
# cache.get(4);       // returns 4


# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/lru-cache
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
