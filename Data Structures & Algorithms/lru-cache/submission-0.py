# LRUCache class

# clarifications
# 1 < capacity < 3000
# well formed input? yes
# 0 <= key <= 10^4
# value <= value <= 10^5
# get and put could be called on empty cache

# data structures
# List[List] where each sublist is [key, value]. tricky at LRU.
# hashmap/dictionary key:value

#how to handle LRU? keep list in order using pointers

# Node with ptr to next and ptr to prev

# hashmap where map.key = key and map.value is ptr to node with value


class ListNode:
    def __init__(self, key = 0, val = 0, prev = None, nxt = None):
        self.key = key
        self.val = val
        
        self.prev = prev
        self.nxt = nxt

class LRUCache:
    def __init__(self, capacity: int):
    # create map
    # global for capacity
        self.hashmap = {}
        self.capacity = capacity
        self.head = ListNode() 
        self.tail = ListNode()
        self.head.nxt = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
    # get: input = int key, output = int value or -1
    # check if key is in map
    # if key exists, 
        # return node.val
    # else return -1
        if key in self.hashmap:
            self.remove(self.hashmap[key])
            self.insert(self.hashmap[key])
            return self.hashmap[key].val
        else:
            return -1

    def put(self, key: int, value: int) -> None:
    # put: input = int key and int value, output = None
    # check if key is in map
        # if key exists
        # remove and insert
        # update node.val
    # else
        # make hashmap entry
        # insert 
    # if exceed capacity, evict LRU key which is at end of linked list
        # if you start at head then go next until you reach capacity

        if key in self.hashmap:
            self.hashmap[key].val = value
            self.remove(self.hashmap[key])
            self.insert(self.hashmap[key])
        else:
            node = ListNode(key, value)
            self.hashmap[key] = node
            self.insert(node)
        if len(self.hashmap) > self.capacity:
            lru = self.tail.prev
            self.remove(lru)
            del self.hashmap[lru.key]

    def insert(self, node: ListNode) -> None:
        # insert node right after head and fix ptrs
        node.nxt = self.head.nxt
        node.prev = self.head
        self.head.nxt.prev = node
        self.head.nxt = node
    def remove(self, node: ListNode):
        # remove the node and fix ptrs
        node.nxt.prev = node.prev
        node.prev.nxt = node.nxt
        
