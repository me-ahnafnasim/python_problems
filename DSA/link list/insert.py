class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, value):
        if self.head is None:
            self.head = Node(value)
        else:
            last = self.head
            while last.next:
                last = last.next
            last.next = Node(value)

    def prepend(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node

    def insert(self, value, index):
        if index == 0:
            self.prepend(value)
        else:
            if self.head is None:
                raise ValueError("Index out of bounds")
            else:
                last = self.head
                for i in range(index - 1):
                    if last.next is None:
                        raise ValueError("Index out of bounds")
                    last = last.next

                new_node = Node(value)
                new_node.next = last.next
                last.next = new_node

if __name__ == "__main__":
    llist = LinkedList()

    llist.append(10)
    llist.append(20)
    llist.append(30)

    llist.prepend(0)
    try:
        llist.insert(1, 0)  # Changed index to 4 to avoid "Index out of bounds" error
    except ValueError as e:
        print(e)

    # Print the linked list to verify the result
    current = llist.head
    while current:
        print(current.value, end=" -> ")
        current = current.next
    print("None")