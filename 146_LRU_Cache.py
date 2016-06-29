# Design and implement a data structure for Least Recently Used (LRU) cache. It should support the following operations: get and set.

# get(key) - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
# set(key, value) - Set or insert the value if the key is not 
# already present. When the cache reached its capacity, it should invalidate the least recently used item before inserting a new item.


# Python concise solution with comments (Using OrderedDict).




class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.d = collections.OrderedDict()
        self.remain =  capacity
        
    def get(self, key):
        """
        :rtype: int
        """
        if key not in self.d:
            return -1
        v = self.d.pop(key)
        self.d[key] = v
        # set key as the newest one
        return v

    def set(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: nothing
        """
        if key in self.d:
            self.d.pop(key)
        else:
            if self.remain > 0:
                self.remain -= 1
            else:
                self.d.popitem(last = False)
       # The pairs are returned in LIFO order if last is true 
       # or FIFO order if false.

        self.d[key] = value





class LRUCache(object):

    def __init__(self, capacity):
        self.deque = collections.deque([])
        self.dic = {}
        self.capacity = capacity

    def get(self,key):
        if key not in self.dic:
            return -1

        self.deque.remove(key)
        self.deque.append(key)
        return self.dic[key]

    def set(self, key, value):
        if key in self.dic:
            self.deque.remove(key)

        elif len(self.dic) == self.capacity:
            v = self.deque.popleft()
            self.dic.pop(v)

        self.deque.append(key)
        self.dic[key] = value









class LinkedNode:
    
    def __init__(self, key=None, value=None, next=None):
        self.key = key
        self.value = value
        self.next = next

class LRUCache:

    # @param capacity, an integer
    def __init__(self, capacity):
        self.hash = {}
        self.head = LinkedNode()
        self.tail = self.head
        self.capacity = capacity
    
    def push_back(self, node):
        self.hash[node.key] = self.tail
        self.tail.next = node
        self.tail = node
    
    def pop_front(self):
        del self.hash[self.head.next.key]
        self.head.next = self.head.next.next
        self.hash[self.head.next.key] = self.head
        
    # change "prev->node->next...->tail"
    # to "prev->next->...->tail->node"
    def kick(self, prev):
        node = prev.next
        if node == self.tail:
            return
        prev.next = node.next
        if node.next is not None:
            self.hash[node.next.key] = prev
            node.next = None
        self.push_back(node)

    # @return an integer
    def get(self, key):
        if key not in self.hash:
            return -1
        self.kick(self.hash[key])
        return self.hash[key].next.value

    # @param key, an integer
    # @param value, an integer
    # @return nothing
    def set(self, key, value):
        if key in self.hash:
            self.kick(self.hash[key])
            self.hash[key].next.value = value
        else:
            self.push_back(LinkedNode(key, value))
            if len(self.hash) > self.capacity:
                self.pop_front()
        















