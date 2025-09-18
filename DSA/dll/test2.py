def create_list():
    return {'head': None, 'tail': None, 'size': 0}


def add_last(list_state, data):
    """Adds data to the end (tail) of the list."""
    new_node = {'data': data, 'prev': None, 'next': None}
    if list_state["head"] is None:
        list_state['head'] = new_node
        list_state['tail'] = new_node
    else:
        #{'data': 10, 'prev': None, 'next': None}
        new_node['prev'] = list_state['tail']
        list_state['tail']['next'] = new_node
        list_state['tail'] = new_node
    list_state['size'] += 1

def display_forward(link_list):
    current = link_list["head"]
    while current:
        print(current["data"], end=" <-> " if current["next"] else "\n")
        current = current["next"]
        print(current)

# Correct usage:
dll = create_list()  # Initialize an empty list, NOT a node
add_last(dll, 10)
add_last(dll, 20)
add_last(dll, 30)
add_last(dll, 40)

display_forward(dll)



















