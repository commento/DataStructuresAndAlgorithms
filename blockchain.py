import hashlib


class Block:

    def __init__(self, timestamp, data, previous_hash):
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calc_hash()
        self.next = None

    def calc_hash(self):
        sha = hashlib.sha256()

        hash_str = "We are going to encode this string of data!".encode('utf-8')

        sha.update(hash_str)

        return sha.hexdigest()

class LinkedList:

    def __init__(self):
        self.head = None

    def append(self, block):

        if self.head is None:
            self.head = block
            return

        tmp = self.head
        while tmp.next:
            tmp = tmp.next

        tmp.next = block

    def size(self):
        size = 0
        block = self.head
        while block:
            size += 1
            block = block.next

        return size

# Test Case 1
print("# Test Case 1: Append the first element")

block1 = Block("11:00:00", 11, None)

llist1 = LinkedList()

llist1.append(block1)

print(llist1.size())
# Test Case 2
print("# Test Case 2: Append a second element")

block2 = Block("22:00:00", 22, None)

llist1.append(block2)

print(llist1.size)

# Test Case 3
print("# Test Case 3: Empty LinkedList")

llist2 = LinkedList()

print(llist2.size())