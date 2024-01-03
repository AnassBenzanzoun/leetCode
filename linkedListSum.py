class LinkedList:
    def __init__(self, value):
        self.head = {"value": value, "next": None}
        self.tail = self.head
        self.length = 1

    def append(self, value):
        newNode = {"value": value, "next": None}
        self.tail["next"] = newNode
        self.tail = newNode
        self.length += 1

    def prepend(self, value):
        newNode = {"value": value, "next": self.head}
        self.head = newNode
        self.length += 1

    def insert(self, index, value):
        newNode = {"value": value, "next": None}
        if index >= self.length:
            self.append(value)
        elif index == 0:
            self.prepend(value)
        else:
            leader = self.traverseToIndex(index - 1)
            newNode["next"] = leader["next"]
            leader["next"] = newNode
            self.length += 1

    def traverseToIndex(self, index):
        currentNode = self.head
        counter = 0
        while counter != index:
            currentNode = currentNode["next"]
            counter += 1
        return currentNode

    def printList(self):
        array = []
        currentNode = self.head
        while currentNode != None:
            array.append(currentNode["value"])
            currentNode = currentNode["next"]
        return array


linked = LinkedList(10)
print(linked.head)
linked.append(5)
print(linked.head)
linked.append(16)
print(linked.head)
linked.prepend(1)
print(linked.head)
linked.insert(2, 99)
print(linked.head)


# class Solution(object):
#     def addTwoNumbers(self, l1, l2):
#         dummy_head = ListNode(0)
#         current = dummy_head
#         carry = 0

#         while l1 or l2 or carry:
#             sum_val = (l1.val if l1 else 0) + (l2.val if l2 else 0) + carry
#             carry = sum_val // 10
#             current.next = ListNode(sum_val % 10)
#             current = current.next
#             l1 = l1.next if l1 else None
#             l2 = l2.next if l2 else None

#         return dummy_head.next
