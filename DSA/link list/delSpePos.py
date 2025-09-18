# Define a node of the linked list
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Define the linked list
class LinkedList:
    def __init__(self):
        self.head = None

    # Method to append a new node at the end
    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    # Method to print the linked list
    def print_list(self):
        curr_node = self.head
        while curr_node:
            print(curr_node.data, end=" -> ")
            curr_node = curr_node.next
        print("None")

    # Method to get an element at a specific position
    def get_at_position(self, pos):
        if not self.head:
            print("List is empty")
            return None
        curr_node = self.head
        count = 0
        while curr_node:
            if count == pos:
                return curr_node.data
            curr_node = curr_node.next
            count += 1
        print("Position out of range")
        return None

# Create a linked list
llist = LinkedList()
llist.append(10)
llist.append(20)
llist.append(30)
llist.append(40)

print("Linked List:")
llist.print_list()

# Get element at position 2 (0-based index)
pos = 2
element = llist.get_at_position(pos)
if element is not None:
    print(f"Element at position {pos}: {element}")
