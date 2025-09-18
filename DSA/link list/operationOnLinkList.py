class Node:
    def __init__(self, data):
        self.data = data  # Data part of the node
        self.next = None  # Pointer to the next node (initially None)


class LinkedList:
    def __init__(self):
        self.head = None  # Initialize the head of the list as None

    # Method to append a new node at the end of the list
    def append(self, data):
        new_node = Node(data)
        if not self.head:  # If the list is empty, set the new node as the head
            self.head = new_node
            return
        last = self.head
        while last.next:  # Traverse to the last node
            last = last.next
        last.next = new_node  # Set the next of the last node to the new node
     
NOTE: Without declearing the New_node/from Neuralnine youtube channel
     NOTE:Solve in a diffrent way
     if self.head is None:
        self.head=Node(data)
    else:
        last = self.head
        while last.next
            last = last.next
        last.next = Node(data)


    # Method to prepend a new node at the beginning of the list
    def prepend(self, data):
        first_node = Node(data)
        first_node.next = self.head  # Point the new node's next to the current head
        self.head = first_node  # Update the head to the new node

    



    # Method to insert a node after a given node
    def insert_after_node(self, prev_node, data):
        if not prev_node:  # Check if the previous node exists
            print("Previous node is not in the list")
            return
        new_node = Node(data)
        new_node.next = prev_node.next  # Link the new node to the next of the previous node
        prev_node.next = new_node  # Update the previous node's next to the new node

    # Method to delete a node by value
    def delete_by_value(self, key):
        curr_node = self.head
        if curr_node and curr_node.data == key:  # If the head node is to be deleted
            self.head = curr_node.next
            curr_node = None
            return
        prev = None
        while curr_node and curr_node.data != key:  # Traverse until the key is found
            prev = curr_node
            curr_node = curr_node.next
        if curr_node is None:  # If the key is not found
            print("Key not found in the list")
            return
        prev.next = curr_node.next  # Unlink the node from the list
        curr_node = None

    # Method to delete a node at a specific position
    def delete_at_position(self, pos):
        if not self.head:  # If the list is empty
            print("List is empty")
            return
        curr_node = self.head
        if pos == 0:  # If the head node is to be deleted
            self.head = curr_node.next
            curr_node = None
            return
        count = 0
        prev = None
        while curr_node and count != pos:  # Traverse to the desired position
            prev = curr_node
            curr_node = curr_node.next
            count += 1
        if curr_node is None:  # If the position is out of bounds
            print("Position out of range")
            return
        prev.next = curr_node.next  # Unlink the node from the list
        curr_node = None

    # Method to print the linked list
    def print_list(self):
        if not self.head:  # Check if the list is empty
            print("List is empty")
            return
        curr_node = self.head
        while curr_node:
            print(curr_node.data, end=" -> ")
            curr_node = curr_node.next
        print("None")  # Indicate the end of the list


# Example Usage
if __name__ == "__main__":
    # Create a linked list
    llist = LinkedList()

    # Append elements
    llist.append(1)
    llist.append(2)
    llist.append(3)

    # Prepend an element
    llist.prepend(0)

    # Print the list
    print("After appending and prepending:")
    llist.print_list()  # Output: 0 -> 1 -> 2 -> 3 -> None

    # Insert after a specific node
    llist.insert_after_node(llist.head.next, 1.5)
    print("After inserting 1.5 after 1:")
    llist.print_list()  # Output: 0 -> 1 -> 1.5 -> 2 -> 3 -> None

    # Delete a node by value
    llist.delete_by_value(1.5)
    print("After deleting 1.5:")
    llist.print_list()  # Output: 0 -> 1 -> 2 -> 3 -> None

    # Delete a node at position
    llist.delete_at_position(1)
    print("After deleting node at position 1:")
    llist.print_list()  # Output: 0 -> 2 -> 3 -> None