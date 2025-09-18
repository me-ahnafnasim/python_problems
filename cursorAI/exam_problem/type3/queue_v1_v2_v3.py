# A queue is stored in a doubly linked list implemented using a dictionary of dictionaries like, for example,
# dll = {
#     'head': {'prev': None, 'next': 12},
#     12: {'prev': 'head', 'next': 20},
#     20: {'prev': 12, 'next': 15},
#     15: {'prev': 20, 'next': 2},
#     2: {'prev': 15, 'next': 'tail'},
#     'tail': {'prev': 2, 'next': None}
# }

# Implement the Python function dsc(list1, v1, v2, v3) that:
# 1) Creates an empty doubly linked list named dll,
# 2) Inserts the (possibly many) elements contained in the parameter list1 so as to implement a queue,
# 3) Adds the arguments v1 and v2 to the queue,
# 4) Removes two elements from the queue,
# 5) Inserts the argument v3,
# 6) Returns the resulting doubly linked list dll.


def dsc(list1, v1, v2, v3):
    dll = {
        'head': {'prev': None, 'next': 'tail'},
        'tail': {'prev': 'head', 'next': None}
    }

    # Step 2: Insert elements from list1
    for value in list1:
        new_key = str(value)
        prev_node = dll['tail']['prev']
        dll[new_key] = {
            'prev': prev_node,
            'next': 'tail'
        }
        dll[prev_node]['next'] = new_key
        dll['tail']['prev'] = new_key

    # Step 3: Add v1 and v2
    for value in [v1, v2]:
        new_key = str(value)
        prev_node = dll['tail']['prev']
        dll[new_key] = {
            'prev': prev_node,
            'next': 'tail'
        }
        dll[prev_node]['next'] = new_key
        dll['tail']['prev'] = new_key

    # Step 4: Remove two elements from the front
    for _ in range(2):
        if dll['head']['next'] != 'tail':
            node_to_remove = dll['head']['next']
            next_node = dll[node_to_remove]['next']
            dll['head']['next'] = next_node
            dll[next_node]['prev'] = 'head'
            del dll[node_to_remove]

    # Step 5: Insert v3
    new_key = str(v3)
    prev_node = dll['tail']['prev']
    dll[new_key] = {
        'prev': prev_node,
        'next': 'tail'
    }
    dll[prev_node]['next'] = new_key
    dll['tail']['prev'] = new_key

    return dll

list1 = [10, 20, 30, 40, 50]
v1 = 60
v2 = 70
v3 = 80

print(dsc(list1,v1,v2,v3))