'''
Implement the `RandomizedSet` class:

- `RandomizedSet()` Initializes the `RandomizedSet` object.
- `bool insert(int val)` Inserts an item `val` into the set if not present. Returns `true` if the item was not present, `false` otherwise.
- `bool remove(int val)` Removes an item `val` from the set if present. Returns `true` if the item was present, `false` otherwise.
- `int getRandom()` Returns a random element from the current set of elements (it's guaranteed that at least one element exists when this method is called). Each element must have the **same probability** of being returned.

You must implement the functions of the class such that each function works in **average** `O(1)` time complexity.

**Example 1:**

```
Input
["RandomizedSet", "insert", "remove", "insert", "getRandom", "remove", "insert", "getRandom"]
[[], [1], [2], [2], [], [1], [2], []]
Output
[null, true, false, true, 2, true, false, 2]

Explanation
RandomizedSet randomizedSet = new RandomizedSet();
randomizedSet.insert(1); // Inserts 1 to the set. Returns true as 1 was inserted successfully.
randomizedSet.remove(2); // Returns false as 2 does not exist in the set.
randomizedSet.insert(2); // Inserts 2 to the set, returns true. Set now contains [1,2].
randomizedSet.getRandom(); // getRandom() should return either 1 or 2 randomly.
randomizedSet.remove(1); // Removes 1 from the set, returns true. Set now contains [2].
randomizedSet.insert(2); // 2 was already in the set, so return false.
randomizedSet.getRandom(); // Since 2 is the only number in the set, getRandom() will always return 2.

```

**Constraints:**

- `231 <= val <= 231 - 1`
- At most `2 * 105` calls will be made to `insert`, `remove`, and `getRandom`.
- There will be **at least one** element in the data structure when `getRandom` is called.

**Solution**

1. We are going to use dictionary and arrays to solve this problem
2. We are using dictionary to achieve insertion and deletion in O(1)
    1. to achieve deletion in O(1) in an array you need to know the index of the item to be deleted
3. Dictionary will store the number mapped to it’s index in array
4. We are using array to get the random values. We need to know indices of values to get the random values
5. Deletion
    1. Number is mapped to it’s index in the array
    2. Replace that index with the last element in the array 
    3. Pop last element 
    4. Update last element’s position in the array
'''

class RandomizedSet:

    def __init__(self):
        self.dict = {}
        self.num_list = []
        

    def insert(self, val: int) -> bool:
        if val not in self.dict:
            self.dict[val] = len(self.num_list)
            self.num_list.append(val)
            return True
        
        return False

    def remove(self, val: int) -> bool:
        if val in self.dict:
            index = self.dict[val]

            last = self.num_list[-1]
            self.num_list[index] = last
            self.num_list.pop()
            
            self.dict[last] = index
            del self.dict[val]

            return True

        return False
        

    def getRandom(self) -> int:
        return random.choice(self.num_list)
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()