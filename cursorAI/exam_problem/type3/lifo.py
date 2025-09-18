"""def ds1(listx):
    #initialize double link list
    #take the every single element from the list
    #convert it into string so that you can use it as key
    # generally select the list's  previus node 
    # make the node you wanna insert into the dictionary
    #update the nodes of head and the tail of the dictionary
    # 

    new_node ={
        "head":{"prev": None, "next":"tail"},
        "tail":{"prev":"head", "next": None}
    }

    for value in listx:
        node_key = str(value)
        prev_node =new_node["tail"]["prev"]

        new_node[node_key] = {
            "prev": prev_node,
            "next": "tail",
            "value": value
        }
        new_node[prev_node]["next"] = node_key
        new_node["tail"]["next"] = node_key
        

if __name__ == "__main__":
    # Test with a list of numbers
    test_list = [10, 20, 30, 40, 50]
    result = ds1(test_list)
    print(result)"""

"""
START
  │
  ├─ 1. Initialize doubly linked list:
  │     - Create "head" node: {"prev": None, "next": "tail", "value": "HEAD"}
  │     - Create "tail" node: {"prev": "head", "next": None, "value": "TAIL"}
  │
  ├─ 2. For each element in input list:
  │     │
  │     ├─ 2.1 Convert element to string (to use as dictionary key)
  │     │
  │     ├─ 2.2 Identify previous node (initially points to head, then last added node)
  │     │       - Get via: new_node["tail"]["prev"]
  │     │
  │     ├─ 2.3 Create new node:
  │     │       {
  │     │         "prev": previous_node_key,
  │     │         "next": "tail",
  │     │         "value": element_value
  │     │       }
  │     │
  │     ├─ 2.4 Update connections:
  │     │       - Set previous_node["next"] = new_node_key
  │     │       - Set tail["prev"] = new_node_key
  │     │
  │     └─ (Repeat for next element)
  │
  └─ 3. Return the completed dictionary structure

END

"""




"""def ds1(listx):
    # Initialize the doubly linked list with head and tail
    new_node = {
        "head": {"prev": None, "next": "tail"},
        "tail": {"prev": "head", "next": None}
    }

    for value in listx:
        node_key = str(value)
        # The node before tail is currently the last real node
        prev_node = new_node["tail"]["prev"]
        
        # Create new node
        new_node[node_key] = {
            "prev": prev_node,
            "next": "tail",  # New node points to tail as next
            "value": value
        }
        
        # Update the previous node's next to point to new node
        new_node[prev_node]["next"] = node_key
        
        # Update tail's prev to point to new node
        new_node["tail"]["prev"] = node_key



        #delet the last two nodes so that it can work as lifo

        #check the length of the list
        # (the operation is only possible if the length of the list is greater than 2)
        #select the last two nodes in general which are the befor tail and one step before the first node
        #update the connections of the last two nodes
        #del the last two nodes

        if len(listx) >= 2:

            first_node = new_node["tail"]["prev"]
            print(first_node)
            second_node = new_node[first_node]["prev"]
            print(second_node)

            new_node["tail"]["prev"] = new_node[second_node]["prev"]
            new_node[new_node[second_node]["prev"]]["next"] = "tail"
           

            del new_node[first_node]
            del new_node[second_node]


        return new_node

if __name__ == "__main__":
    # Test with a list of numbers
    test_list = [10, 20, 30, 40, 50, 60]
    result = ds1(test_list)
    print(result)
"""


def ds1(listx):
    # Initialize the doubly linked list
    new_node = {
        "head": {"prev": None, "next": "tail"},
        "tail": {"prev": "head", "next": None}
    }

    # Build the list
    for value in listx:
        node_key = str(value)
        prev_node = new_node["tail"]["prev"]
        
        new_node[node_key] = {
            "prev": prev_node,
            "next": "tail",
            "value": value
        }
        
        new_node[prev_node]["next"] = node_key
        new_node["tail"]["prev"] = node_key

    # Delete last two nodes if list has ≥2 elements
    if len(listx) >= 2:
        first_node = new_node["tail"]["prev"]          # Last node (e.g., "50")
        second_node = new_node[first_node]["prev"]     # Second-last node (e.g., "40")

        # Update tail's prev to skip the last two nodes
        new_node["tail"]["prev"] = new_node[second_node]["prev"]
        
        # Update the new last node's next to point to tail
        new_node[new_node[second_node]["prev"]]["next"] = "tail"

        # Delete the two nodes
        del new_node[first_node]
        del new_node[second_node]

    return new_node




print(ds1([10, 20, 30, 40, 50, 60]))




