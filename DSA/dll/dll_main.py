# Initialize an empty doubly linked list
linked_list = {
    "head": None,
    "tail": None
}

# Function to create a new node
def create_node(data):
    return {
        "data": data,
        "prev": None, 
        "next": None
    }


# Function to insert at the end
def insert_end(linked_list, data):
    new_node = create_node(data)
    if linked_list["head"] is None:
        linked_list["head"] = new_node
        linked_list["tail"] = new_node
    else:
        tail = linked_list["tail"]
        print("1st:",tail)
        tail["next"] = new_node
        new_node["prev"] = tail
        linked_list["tail"] = new_node

# Function to insert at the beginning
def insert_begin(linked_list, data):
    new_node = create_node(data)
    if linked_list["head"] is None:
        linked_list["head"] = new_node
        linked_list["tail"] = new_node
    else:
        head = linked_list["head"]
        new_node["next"] = head
        head["prev"] = new_node
        linked_list["head"] = new_node

# Function to delete from the beginning
def delete_begin(linked_list):
    if linked_list["head"] is None:
        return
    head = linked_list["head"]
    if head["next"] is None:
        linked_list["head"] = None
        linked_list["tail"] = None
    else:
        linked_list["head"] = head["next"]
        linked_list["head"]["prev"] = None

# Function to delete from the end
def delete_end(linked_list):
    if linked_list["tail"] is None:
        return
    tail = linked_list["tail"]
    if tail["prev"] is None:
        linked_list["head"] = None
        linked_list["tail"] = None
    else:
        linked_list["tail"] = tail["prev"]
        linked_list["tail"]["next"] = None

# Function to display from head to tail
def display_forward(linked_list):
    current = linked_list["head"]
    while current:
        print(current["data"], end=" <-> " if current["next"] else "\n")
        current = current["next"]

# Function to display from tail to head
def display_backward(linked_list):
    current = linked_list["tail"]
    while current:
        print(current["data"], end=" <-> " if current["prev"] else "\n")
        current = current["prev"]

# Example usage
insert_end(linked_list, 10)
insert_end(linked_list, 20)



print("Forward:")
display_forward(linked_list)

print("Backward:")
display_backward(linked_list)

delete_begin(linked_list)
delete_end(linked_list)

print("After Deletion Forward:")
display_forward(linked_list)
