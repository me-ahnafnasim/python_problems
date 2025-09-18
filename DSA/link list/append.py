# Step 1: Define two classes - one for the Node and one for the LinkedList

# Class for creating nodes
class Node:
    def __init__(self, data):
        self.data = data  # Store the data
        self.next = None  # Initialize the next pointer to None

# Class for the LinkedList
class LinkedList:
    def __init__(self):
        self.head = None  # Initialize the head of the list to None (empty list)

    # Function to append a new node to the end of the list
    def append(self, data):
        # Create an instance of Node which will store the data
        new_node = Node(data)

        # Check if the list is empty
        if self.head is None:  # If the list is empty
            self.head = new_node  # Set the new node as the head
            return  # Exit the function

        # If the list is not empty, traverse to the last node
        curr_node = self.head  # Start from the head of the list

        # Run a while loop to track the elements until we reach the last node
        while curr_node.next:  # While curr_node.next is not None
            curr_node = curr_node.next  # Move to the next node

        # Once the last node is reached, append the new node
        curr_node.next = new_node  # Set the next of the last node to the new node

    # Optional: A utility function to print the list (for testing purposes)
    def print_list(self):
        curr_node = self.head
        while curr_node:
            print(curr_node.data, end=" -> ")  # Print the data of the current node
            curr_node = curr_node.next  # Move to the next node
        print("None")  # Indicate the end of the list


# Example usage:
if __name__ == "__main__":
    # Create a new linked list
    ll = LinkedList()

    # Append elements to the list
    ll.append(10)
    ll.append(20)
    ll.append(30)
    ll.append(40)
    ll.append(60)
    ll.append(70)

    # Print the list
    ll.print_list()