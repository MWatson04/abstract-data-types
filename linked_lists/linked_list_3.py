class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, value):
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
            print("Head node created:", self.head.value)
            return

        node = self.head
        while node.next is not None:
            node = node.next

        node.next = new_node
        print("Appended new Node with value:", node.next.value)

    def prepend(self, value):
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
            print("Head Node Created:", self.head.value)
            return

        if self.head is not None:
            new_node.next = self.head
            print("Prepended New Head Node With Value:", new_node.value)
            print("Node Following New Head:", new_node.next.value)

        self.head = new_node
        print("New Head Node:", new_node.value)


llist = LinkedList()
llist.prepend("First Node")
llist.prepend("Inserted New First Node")

