'''
Design a data structure to store the strings' count with the ability to return the strings with minimum and maximum counts.

Implement the `AllOne` class:

- `AllOne()` Initializes the object of the data structure.
- `inc(String key)` Increments the count of the string `key` by `1`. If `key` does not exist in the data structure, insert it with count `1`.
- `dec(String key)` Decrements the count of the string `key` by `1`. If the count of `key` is `0` after the decrement, remove it from the data structure. It is guaranteed that `key` exists in the data structure before the decrement.
- `getMaxKey()` Returns one of the keys with the maximal count. If no element exists, return an empty string `""`.
- `getMinKey()` Returns one of the keys with the minimum count. If no element exists, return an empty string `""`.

**Note** that each function must run in `O(1)` average time complexity.
'''

class Node:
    def __init__(self, freq):
        self.freq = freq
        self.prev = None
        self.next = None
        self.keys = set()


class AllOne:

    def __init__(self):
        self.head = Node(0)
        self.tail = Node(0)
        self.head.next = self.tail
        self.tail.prev = self.head

        self.char_map = {}
        

    def inc(self, key: str) -> None:
        if key in self.char_map:
            node = self.char_map[key]
            freq = node.freq
            node.keys.remove(key)

            next_node = node.next

            if next_node == self.tail or next_node.freq != freq + 1:
                new_node = Node(freq + 1)
                new_node.keys.add(key)

                new_node.prev = node
                new_node.next = next_node

                node.next = new_node
                next_node.prev = new_node

                self.char_map[key] = new_node
            else:
                next_node.keys.add(key)
                self.char_map[key] = next_node
            
            if not node.keys:
                self.removeNode(node)
        
        else:
            first_node = self.head.next

            if first_node == self.tail or first_node.freq > 1:
                new_node = Node(1)
                new_node.keys.add(key)

                new_node.prev = self.head
                new_node.next = first_node

                self.head.next = new_node
                first_node.prev = new_node

                self.char_map[key] = new_node
            else:
                first_node.keys.add(key)
                self.char_map[key] = first_node
                


    def dec(self, key: str) -> None:
        if key not in self.char_map:
            return
        
        node = self.char_map[key]
        node.keys.remove(key)

        freq = node.freq

        if freq == 1:
            del self.char_map[key]
        else:
            prev_node = node.prev

            if prev_node == self.head or prev_node.freq != freq - 1:
                new_node = Node(freq - 1)
                new_node.keys.add(key)

                new_node.prev = prev_node
                new_node.next = node

                prev_node.next = new_node
                node.prev = new_node

                self.char_map[key] = new_node
            else:
                prev_node.keys.add(key)
                self.char_map[key] = prev_node
            
        if not node.keys:
            self.removeNode(node)

        
    def getMaxKey(self) -> str:
        if self.tail.prev == self.head:
            return ""
        else:
            return next(
                iter(self.tail.prev.keys)
            )
        

    def getMinKey(self) -> str:
        if self.head.next == self.tail:
            return ""
        else:
            return next(
                iter(self.head.next.keys)
            )
    
    def removeNode(self, node):
        prev_node = node.prev
        next_node = node.next

        prev_node.next = next_node
        next_node.prev = prev_node