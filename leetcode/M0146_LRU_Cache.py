class DequeNode:
    def __init__(self, k = 0, x = 0):
        self.key = k
        self.val = x
        self.prev = None
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
            self.head.prev = node
        self.head = node
        if not self.tail: self.tail = node

    def __update(self, node: DequeNode):
        if node is self.head: return
        node.prev.next = node.next
        if node is self.tail: self.tail = node.prev
        else: node.next.prev = node.prev
        node.prev = None
        self.__insert(node)

    def __pop(self):
        node = self.tail
        if node is self.head: self.head, self.tail = None, None
        else: self.tail, node.prev.next = node.prev, None
        return node


class LRUCacheGuard:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        self.pool = {}
        self.head = DequeNode()
        self.head.next = self.head
        self.head.prev = self.head

    def get(self, key: int) -> int:
        if key in self.pool:
            node = self.pool[key]
            self._move_to_head(node)
            return node.val
        else: return -1

    def put(self, key: int, value: int) -> None:
        if key in self.pool:
            self.pool[key].val = value
            self._move_to_head(self.pool[key])
        else:
            node = DequeNode(key, value)
            self.pool[key] = node
            self._add_node(node)
            if self.size < self.capacity: self.size += 1
            else: self.pool.pop(self._pop_tail().key)

    def _add_node(self, node):
        self.head.next.prev, node.next = node, self.head.next
        self.head.next, node.prev = node, self.head

    def _remove_node(self, node):
        node.next.prev, node.prev.next = node.prev, node.next
        return node

    def _move_to_head(self, node):
        self._remove_node(node)
        self._add_node(node)

    def _pop_tail(self):
        return self._remove_node(self.head.prev)


from collections import OrderedDict

class LRUCacheOrderedDict(OrderedDict):
    def __init__(self, capacity: int):
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key not in self: return -1
        self.move_to_end(key)
        return self[key]

    def put(self, key: int, value: int) -> None:
        if key in self: self.move_to_end(key)
        self[key] = value
        if len(self) > self.capacity: self.popitem(last=False)


cache = LRUCacheOrderedDict(2)
cache.put(1, 1)
cache.put(2, 2)
print(1, cache.get(1))
cache.put(3, 3)
print(-1, cache.get(2))
cache.put(4, 4)
print(-1, cache.get(1))
print(3, cache.get(3))
print(4, cache.get(4))
cache.put(2, 1)
cache.put(2, 2)
print(2, cache.get(2))
cache.put(1, 1)
cache.put(4, 1)
print(-1, cache.get(2))


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
