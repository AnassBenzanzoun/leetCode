import math


class BinarySearch:
    def __init__(self, numbers, needle):
        self.numbers = numbers
        self.needle = needle
        self.low = 0
        self.high = len(numbers) - 1
        self.mid = 0
        self.value = 0
        self.search()

    def search(self):
        while self.low <= self.high:
            self.mid = int(math.floor(self.low + (self.high - self.low)) / 2)
            print(self.mid)
            self.value = self.numbers[self.mid]
            if self.value == self.needle:
                return self.mid
            elif self.value > self.needle:
                self.low = self.mid + 1


binary = BinarySearch([1, 2, 3, 4, 5, 6, 7, 8, 9], 5)
print(binary)
