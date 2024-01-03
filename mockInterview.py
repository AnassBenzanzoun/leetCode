# 1- insert a value (no duplicates)
# 2- delete a value
# 3- getRandom value that is already inserted (equal probability)


import random


class Store:
    def __init__(
        self,
    ):
        self.values = []
        self.map = {}

    # efficient insert, delete, getRandom with O(1) time complexity
    def insert(self, value):
        if value not in self.map:
            self.values.append(value)
            self.map[value] = len(self.values) - 1
        return f"map: {self.map}, values {self.values}"

    def delete(self, value):
        if value not in self.map:
            return
        # swap the value to be deleted with the last value in the list
        index = self.map[value]
        last_value = self.values[-1]
        self.values[-1] = value
        self.values[index] = last_value
        self.map[last_value] = index
        self.values.pop()  # remove last value which is way faster than removing from the middle
        del self.map[value]
        return f"map: {self.map}, values {self.values}"

    def getRandom(self):
        return random.choice(self.values)


store = Store()

# Example 1
inserts = [3, 4, 4, 5]
for insert in inserts:
    print(store.insert(insert))
    print(store.getRandom())

print(store.delete(4))

# what if the values are not unique?
# if the values are not unique we would use the hashmap to store a list of indices for each value
# {1: [0, 2], 2: [1], 3: [3, 4]}


class StoreWithDuplicates:
    def __init__(
        self,
    ):
        self.values = []
        self.map = set()

    # efficient insert, delete, getRandom with O(1) time complexity
    def insert(self, value):
        self.values.append(value)
        self.map[value].append(len(self.values) - 1)
        return f"map: {self.map}, values {self.values}"

    def delete(self, value):
        if value not in self.map:
            return
        # swap the value to be deleted with the last value in the list
        index = self.map[value][0]
        last_value = self.values[-1]
        self.values[-1] = value
        self.values[index] = last_value
        self.map[last_value].append(index)
        self.values.pop()  # remove last value which is way faster than removing from the middle
        del self.map[value]
        return f"map: {self.map}, values {self.values}"

    def getRandom(self):
        return random.choice(self.values)
