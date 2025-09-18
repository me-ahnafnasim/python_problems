# Node representation as a dictionary
def create_node(item=None, next_node=None):
    return {"item": item, "next_node": next_node}

# Singly Linked List represented by a dictionary with a 'head' key
linked_list = {"head": None}

# Function to append an item to the left of the list
def appendleft(item):
    new_node = create_node(item, linked_list["head"])
    linked_list["head"] = new_node
    print(f"Congrats! {item} has been added to the left.")

# Function to append an item to the end of the list
def append(item):
    new_node = create_node(item)
    if linked_list["head"] is None:
        linked_list["head"] = new_node
    else:
        current = linked_list["head"]
        while current["next_node"]:
            current = current["next_node"]
        current["next_node"] = new_node
    print(f"Congrats! {item} has been appended.")

# Function to insert an item at a specific position
def insert(position, item):
    size = get_size()
    if position == 0:
        appendleft(item)
        print(f"{item} inserted at position {position}.")
    elif position == size:
        append(item)
        print(f"{item} inserted at position {position}.")
    elif position > size:
        print("Index out of range.")
    else:
        current = linked_list["head"]
        index = 0
        while current:
            if index == position - 1:
                new_node = create_node(item, current["next_node"])
                current["next_node"] = new_node
                print(f"{item} inserted at position {position}.")
                break
            current = current["next_node"]
            index += 1

# Function to check if the list is empty
def is_empty():
    return linked_list["head"] is None

# Function to get the size of the list
def get_size():
    count = 0
    current = linked_list["head"]
    while current:
        count += 1
        current = current["next_node"]
    return count

# Function to get the index of an item in the list
def index(item):
    current = linked_list["head"]
    index = 0
    while current:
        if current["item"] == item:
            return index
        current = current["next_node"]
        index += 1
    return None

# Function to search for an item in the list
def search(item):
    current = linked_list["head"]
    while current:
        if current["item"] == item:
            return True
        current = current["next_node"]
    return False

# Function to remove the first item from the list
def popleft():
    if is_empty():
        print("Empty list")
    else:
        current = linked_list["head"]
        temp = current["item"]
        linked_list["head"] = current["next_node"]
        del current
        return temp

# Function to remove the last item from the list
def pop():
    if is_empty():
        print("Empty list")
    else:
        current = linked_list["head"]
        previous = None
        while current["next_node"]:
            previous = current
            current = current["next_node"]
        if previous is None:
            linked_list["head"] = None
        else:
            previous["next_node"] = None
        temp = current["item"]
        del current
        return temp

# Function to remove a specific item from the list
def remove(item):
    if is_empty():
        print("Empty list")
    else:
        current = linked_list["head"]
        previous = None
        found = False
        while current and not found:
            if current["item"] == item:
                found = True
            else:
                previous = current
                current = current["next_node"]
        if current is None:
            print("Item not found")
        elif previous is None:
            popleft()
            print(f"{item} removed.")
        else:
            previous["next_node"] = current["next_node"]
            del current
            print(f"{item} removed.")

# Function to print the list
def printlist():
    if is_empty():
        print("Empty list")
    else:
        current = linked_list["head"]
        while current:
            print(current["item"])
            current = current["next_node"]

# Main function to interact with the user
def main():
    while True:
        print("\n1. Append to Left \n2. Append \n3. Insert \n4. Get Size \n5. Search \n6. Get Index \n7. Remove \n8. Pop from Left \n9. Pop \n10. Print List \n11. Quit")
        print("\nWhat do you wanna do now?")
        case = int(input())
        if case == 1:
            item = input("Input item, you wanna append to left of list: ")
            appendleft(item)
        elif case == 2:
            item = input("Input item, you wanna append to list: ")
            append(item)
        elif case == 3:
            position = int(input("Input position: "))
            item = input("Input item, you wanna push to list: ")
            insert(position, item)
        elif case == 4:
            print(f"There are {get_size()} items in the list.")
        elif case == 5:
            item = input("Input item, you wanna search in list: ")
            print(search(item))
        elif case == 6:
            item = input("Input item, you wanna know its index: ")
            idx = index(item)
            if idx is not None:
                print(f"{item} is in index number {idx}")
            else:
                print(f"{item} not found in the list.")
        elif case == 7:
            item = input("Input item, you wanna remove: ")
            remove(item)
        elif case == 8:
            if is_empty():
                print("Empty list")
            else:
                item = popleft()
                print(f"{item} removed.")
        elif case == 9:
            if is_empty():
                print("Empty list")
            else:
                item = pop()
                print(f"{item} removed.")
        elif case == 10:
            printlist()
        elif case == 11:
            print("The script is gonna quit.")
            break
        else:
            print("Oops! Wrong Choice.")

if __name__ == "__main__":
    main()