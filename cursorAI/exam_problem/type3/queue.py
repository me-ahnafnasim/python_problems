"""
#note: added at the back (enqueue) and removed from the front (dequeue),
You are given a Python list of elements as input. Your task is to:

1 - Create an empty doubly linked list, implemented using a dictionary of dictionaries. The structure of the doubly linked list should follow this format:

{
    'head': {'prev': None, 'next': first_key},
    key1: {'prev': 'head', 'next': key2},
    key2: {'prev': key1, 'next': key3},
    ...
    'tail': {'prev': last_key, 'next': None}
}

2 - Insert all elements from the input list into the doubly linked list to form a queue.  
(That is, insert at the end of the queue.)

3 - Remove two elements from the front of the queue (i.e., dequeue twice from the front).

4 - Return the resulting doubly linked list as a dictionary.
"""


def ds1(listx):
    dll ={
        "head":{"prev":None, "next":"tail"},
        "tail":{"prev":"head", "tail":None}
    }

    for value in listx:
        node_key =str(value)
        prev_node =dll["tail"]["prev"]

        dll[node_key] ={
            "prev":prev_node,
            "next":"tail",
            "value": value
        }

        dll[prev_node]["next"] = node_key
        dll["tail"]["prev"] = node_key
    
    if len(listx)>=2:
        for _ in range(2):
            node_after_head = dll["head"]["next"]
            next_node = dll[node_after_head]["next"]
            dll["head"]["next"] = next_node
            #next_node er sathe ["prev"] ar [prev_node] er sathe ["next"]
            dll[next_node]["prev"] = "head"
            del dll[node_after_head]
        return dll
    

print(ds1([10,20,30,40,50]))