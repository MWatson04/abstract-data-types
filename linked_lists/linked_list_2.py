class DoublyNode:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, value):
        new_node = DoublyNode(value)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
            print("Head Node Created:", self.head.value)
            return

        new_node.prev = self.tail
        self.tail.next = new_node
        self.tail = new_node
        print("Appended New Node With Value:", self.tail.value)

dllist = DoublyLinkedList()
dllist.append("First Node")
dllist.append("Second Node")
dllist.append("Third Node")
