def initilize_node():
    return {"head":None, "tail":None}

def add_node_in_tail(link_list, data):
    new_node ={"data": data, "next": None}

    if link_list["head"] is None:
        link_list["head"] = new_node
        link_list["tail"] = new_node
    
    else:
        link_list["tail"]["next"] = new_node
        link_list["tail"] = new_node




def add_node_at_head(link_list, data):
    new_node = {'data': data, 'next': None}  # Create new node
    
    if link_list['head'] is None:  # If list is empty, jodi list khali thake
        # If the list is empty, the new node becomes both head and tail
        link_list['head'] = new_node
        link_list['tail'] = new_node
    else:
        # if the list is not empty
        new_node['next'] = link_list['head']  # Point new node to current head
        link_list['head'] = new_node  # Update head to be the new node

"""
Start

Create a new node

Check if position == 0

    If yes:

    Set new_node's next to head

    Update head to new_node

    If tail is None, set tail to new_node

    End

Else:

   Set current = head, index = 0

   Traverse while current is not None and index < position - 1:

   Move current to next node

   Increment index

   After traversal, check:

   If current is None: Raise IndexError

   Else:

   Insert new node

   If new_node's next is None, update tail

  End

"""
"""
1) take three argument-->> link_list, data, position
2) Create a node
3) check if position ==0
4) if yes then add a node in the head and check if the link was empty for updating the tail

5) else:
6)Traversal the link_list and update the index
"""

def insert_at_position(linked_list, value, position):
    # Create the new node
    new_node = {"data": value, "next": None}

    # Case 1: Insert at the head (position 0)
    if position == 0:
        new_node["next"] = linked_list["head"]
        linked_list["head"] = new_node
        # If the list was empty, update the tail
        if linked_list["tail"] is None:
            linked_list["tail"] = new_node
        return

    # Case 2: Insert at a specific position
    current = linked_list["head"]
    index = 0

    # Traverse to find the node before the desired position
    while current is not None and index < position - 1:
        current = current["next"]
        index += 1

    # Check if the position is valid
    if current is None:
        raise IndexError("Position out of bounds")

    # Insert the new node
    new_node["next"] = current["next"]
    current["next"] = new_node

    # If the new node is inserted at the end, update the tail
    if new_node["next"] is None:
        linked_list["tail"] = new_node





def find_element(linked_list, value):
    current = linked_list['head']  # Start from the head of the list

    # Traverse the list
    while current is not None:
        if current['data'] == value:  # Check if the current node contains the target value
            return True  # Element found
        current = current['next']  # Move to the next node

    return "Not Found"  # Element not found





"""
To delete a node with a specific value in a singly linked list , you need to consider three main cases based on the position of the node to be deleted:

1) Deleting the First Node (Head) :
If the node to be deleted is the first node, you need to update the head pointer to point to the next node.
If the list has only one node, you also need to update the tail pointer to None.

2) Deleting a Middle Node :
If the node to be deleted is in the middle of the list, you need to update the next pointer of the previous node to bypass the current node.
     -->If previous is not None, it means the node to be deleted is not the first node.
     -->Update previous['next'] to bypass current and point to current['next'].
     -->If the node being deleted is the last node (current['next'] is None), update linked_list['tail'] to previous.

3)Deleting the Last Node (Tail) :
If the node to be deleted is the last node, you need to update the tail pointer to point to the previous node.
"""

def delete_node(linked_list, value):
    current = linked_list['head']
    previous = None

    # Traverse the list to find the node to delete
    while current is not None:
        #print("current data:",current["data"])
        if current['data'] == value:  # Node found
            if previous is None: #Yes, previous is None indicates that the current node is the first node in the linked list.
                # Case 1: Deleting the first node (head)
                linked_list['head'] = current['next']
                if linked_list['head'] is None:  # List becomes empty
                    linked_list['tail'] = None
            else:
                # Case 2: Deleting a middle or last node
                previous['next'] = current['next']
                if current['next'] is None:  # Deleting the last node
                    linked_list['tail'] = previous
            return True  # Node deleted successfully
        # Move to the next node
        #This line updates the previous pointer to point to the current node before moving forward.
        previous = current
        #This line moves the current pointer to the next node in the list.
        current = current['next']

    return False  # Node not found





def print_node(link_list):
    current = link_list["head"]
    while current is not None:
            print(current["data"], end="->")
            current = current["next"]
    print("None")



link_list = initilize_node()

add_node_at_head(link_list, 6)
add_node_at_head(link_list, 5)

print("Adding nodes to the linked list...")
add_node_in_tail(link_list, 10)
add_node_in_tail(link_list, 20)
add_node_in_tail(link_list, 30)
add_node_in_tail(link_list, 40)


insert_at_position(link_list, 15, 0)



"""search_and_delete(link_list, 20)
search_and_delete(link_list, 10)"""
delete_node(link_list, 30)

print("find element:")
print(find_element(link_list, 30))
print(find_element(link_list, 40))


print("Linked List:")
print_node(link_list)

