class Node:
    def __init__(self, key, val):
        self.val = val
        self.key = key
        self.next = None
        self.prev = None
    def __str__(self):
        return 'key: '+str(self.key) + ' val: '+ str(self.val)


class LRUCache:

    def __init__(self, capacity: int):
        self.size = capacity
        self.n_items = 0
        self.head = Node(None, None)
        self.hash_map = {}
        self.tail = self.head

    def get(self, key: int) -> int:
        if key in self.hash_map:
            node = self.hash_map[key]
            if node.prev is None:
                return node.val
            if node.next is None:
                self.tail = node.prev
                self.tail.next = None
            node.prev.next = node.next
            if node.next is not None:
                node.next.prev = node.prev
            node.next = self.head
            self.head.prev = node
            self.head = node
            self.head.prev = None
            return node.val
        return -1

    def put(self, key: int, value: int) -> None:
        #already there
        if key in self.hash_map:
            node = self.hash_map[key]
            node.val = value
            if node.prev is None:
                return
            if node.next is None:
                self.tail = node.prev
                self.tail.next = None
            node.prev.next = node.next
            if node.next is not None:
                node.next.prev = node.prev
            node.next = self.head
            self.head.prev = node
            self.head = node
            self.head.prev = None
        # empty cache
        elif self.head.val is None:
            self.n_items += 1
            self.head.val = value
            self.head.key = key
            self.hash_map[key] = self.head
        # cache with extra room
        elif self.n_items < self.size:
            self.n_items += 1
            node = Node(key, value)
            node.next = self.head
            self.head.prev = node
            self.head = node
            self.hash_map[key] = node
        # full cache
        else:
            node = Node(key, value)
            node.next = self.head
            self.head.prev = node
            self.head = node
            del self.hash_map[self.tail.key]
            self.hash_map[key] = node
            self.tail = self.tail.prev
            self.tail.next = None
    def __str__(self):
        return str(self.hash_map) + ' head: ' + str(self.head) + ' tail: ' + str(self.tail)

if __name__ == '__main__':
    cache = LRUCache(3)
    cache.put(1, 1)
    cache.put(2, 2)
    cache.put(3, 3)
    cache.put(4, 4)
    print(cache.get(4))
    print(cache.get(3))
    print(cache.get(2))
    print(cache.get(1))
    cache.put(5, 5)
    print(cache.get(1))
    print(cache.get(2))
    print(cache.get(3))
    print(cache.get(4))
    print(cache.get(5))