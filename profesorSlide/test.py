

# Function to create an empty linked list-like structure
def create():
    llist = dict()
    llist['head'] = 'tail'  # Initialize 'head' pointing to 'tail'
    llist['tail'] = "Null"  # Initialize 'tail' pointing to 0
    return llist

# Function to add an element at the beginning of the linked list
def add_first(llist, element):
    llist[element] = llist['head']  # Link the new element to the current 'head'
    llist['head'] = element         # Update 'head' to point to the new element
    return llist


def add_last(llist, element):
    # Start at the head of the list
    current_node = 'head'
    
    # Traverse until we find the node before tail
    while llist[current_node] != 'tail':
        current_node = llist[current_node]
    
    # Insert the new element
    llist[element] = 'tail'          # New node points to tail
    llist[current_node] = element    # Previous last node points to new node
    
    return llist

# Function to delete the first element of the linked list
def del_first(llist):
    if llist['head'] == 'tail':  # Check if the list is empty
        print("List is empty. Nothing to delete.")
        return llist

    x = llist['head']          # Get the current first element
    llist['head'] = llist[x]   # Update 'head' to point to the next element
    del llist[x]               # Remove the first element from the dictionary
    return llist

# Function to traverse the linked list and return a path of tuples
def itraverse(llist):
    curr = 'head'
    path = []
    path.append((0, curr))  # Start with 'head' as index 0
    k = 1
    while curr != 'tail':
        next_node = llist[curr]
        path.append((k, next_node))
        curr = next_node
        k += 1
    return path

# Modified printall() function to display only the elements in a clean format
def printall(llist):
    curr = llist['head']  # Start from the first element after 'head'
    elements = []         # List to store the elements

    while curr != 'tail':
        elements.append(curr)  # Add the current element to the list
        curr = llist[curr]     # Move to the next element

    # Join the elements with '->' for a clean output
    print(" -> ".join(elements))

# Example Usage
if __name__ == "__main__":
    # Step 1: Create an empty linked list
    llist = create()
    print("Initial List:")
    printall(llist)

    # Step 2: Add elements to the list
    llist = add_first(llist, 'C')  # Add 'C' first
    llist = add_first(llist, 'B')  # Add 'B' next
    llist = add_first(llist, 'A')  # Add 'A' last
    print("\nAfter adding elements at the front:")
    printall(llist)

    # Step 3: Add an element at the end
    llist = add_last(llist, 'D')  # Add 'D' at the end
    print("\nAfter adding 'D' at the end:")
    printall(llist)

    # Step 4: Traverse the list and print the path
    print("\nTraversal Path:")
    path = itraverse(llist)
    for step in path:
        print(step)

    # Step 5: Delete the first element
    llist = del_first(llist)  # Delete 'A'
    print("\nAfter deleting the first element:")
    printall(llist)